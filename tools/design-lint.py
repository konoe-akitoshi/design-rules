#!/usr/bin/env python3
"""
design-lint — ガイドラインの「機械判定できる規則」だけを検査する最小リンタ。

思想: ルールは"読ませる"だけでは生成を縛れない（AIの事前分布が勝つ）。
      検査可能な規則は実行可能なテストにして、違反を名指し→その箇所だけ直す。
      （主観的判断＝テンプレ臭さ/eyebrowの意味性などは別途、独立した批評パスで。）

各チェックは出典規則にトレースする:
  prohibited.md … AI生成が外しがちな禁止形
  guidelines/   … 自己完結デザインガイドライン

使い方:
  python tools/design-lint.py examples/benchmark/01-granola.html
  python tools/design-lint.py examples/benchmark/*.html
終了コード: error 件数（0=合格）。warn/info は終了コードに影響しない。
"""
import sys, re, glob, math

# severity: ERROR=必ず直す / WARN=要確認 / INFO=参考
ERROR, WARN, INFO = "ERROR", "WARN", "INFO"

def lines_of(text, pat, flags=re.I):
    out = []
    for m in re.finditer(pat, text, flags):
        out.append(text.count("\n", 0, m.start()) + 1)
    return out

def hex_to_hsl(h):
    h = h.lstrip("#")
    if len(h) == 3: h = "".join(c*2 for c in h)
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn: return 0.0, 0.0, l
    d = mx - mn
    s = d / (1 - abs(2 * l - 1)) if l not in (0, 1) else 0
    if mx == r:   hue = ((g - b) / d) % 6
    elif mx == g: hue = (b - r) / d + 2
    else:         hue = (r - g) / d + 4
    return hue * 60, s, l

def check(text):
    f = []  # (severity, rule, source, n, hint, lines)

    # 1) 純白・純黒（色/地として）— prohibited「text-black の直接使用」/ 01「純白純黒を避ける」
    #    gradient/mask 行の #000/#fff は alpha 用なので除外
    bw = [ln for ln in lines_of(text, r'#(?:000000|000|ffffff|fff)\b')
          if not re.search(r'gradient|mask', text.splitlines()[ln-1], re.I)]
    if bw:
        f.append((WARN, "PURE-BLACK-WHITE", "prohibited / 01-foundations", len(bw),
                  "#000/#fff を色・地に直接使用。ink/地はわずかに色を寄せる", bw))

    # 2) 正方形/均等パディング — prohibited「縦横同値の正方形パディング」
    sq = lines_of(text, r'padding:\s*\d+(?:\.\d+)?px\s*[;}"\']')          # 単値
    eq = [ln for ln in lines_of(text, r'padding:\s*(\d+)px\s+(\d+)px\s*[;}"\']')
          if (lambda m: m and m.group(1) == m.group(2))(
              re.search(r'padding:\s*(\d+)px\s+(\d+)px', text.splitlines()[ln-1]))]
    if sq or eq:
        f.append((WARN, "SQUARE-PADDING", "prohibited / values/spacing", len(sq)+len(eq),
                  "縦横同値の padding。非対称（例 16px 24px = 1:1.5）に", sorted(set(sq+eq))))

    # 3) eyebrow/kicker 過剰 — prohibited「eyebrow（小さい大文字タグライン）の常用」
    eb = lines_of(text, r'class="[^"]*\b(?:eyebrow|kicker|overline|superlabel|sec-kicker|sec-label)\b')
    up = len(re.findall(r'text-transform:\s*uppercase', text, re.I))
    if eb:
        sev = WARN if len(eb) > 4 else INFO
        f.append((sev, "EYEBROW-DENSITY", "prohibited 構造・骨格", len(eb),
                  f"前見出し(eyebrow/kicker)要素が {len(eb)}個 / uppercase宣言 {up}個。"
                  "各々『見出しにない情報(章・号・状態)を運ぶ』か確認し、装飾なら削除", eb))

    # 4) グラデーション地の多用 — prohibited「グラデーション背景の多用」
    #    mask-image / -webkit-mask の gradient は除外（合成用）
    gr = [ln for ln in lines_of(text, r'(?:linear|radial|conic)-gradient')
          if not re.search(r'mask', text.splitlines()[ln-1], re.I)]
    if gr:
        sev = WARN if len(gr) > 3 else INFO
        f.append((sev, "GRADIENT-BG", "prohibited 色彩", len(gr),
                  f"グラデーション {len(gr)}箇所。装飾地は避けソリッド基本（写真スクリムは可）", gr))

    # 5) 強いシャドウ — prohibited「shadow-lg/xl 等の強いシャドウ」
    heavy = []
    for m in re.finditer(r'box-shadow:[^;}]*', text, re.I):
        for blur in re.findall(r'-?\d+px\s+-?\d+px\s+(\d+)px', m.group(0)):
            if int(blur) >= 48:
                heavy.append(text.count("\n", 0, m.start()) + 1)
    if heavy:
        f.append((WARN, "HEAVY-SHADOW", "prohibited AI生成パターン", len(heavy),
                  "blur≥48px の強い影。ヘアライン境界か shadow-sm 相当に", sorted(set(heavy))))

    # 6) img の alt 欠落 — 10-accessibility / WCAG
    noalt = lines_of(text, r'<img\b(?![^>]*\balt=)[^>]*>')
    if noalt:
        f.append((ERROR, "IMG-ALT", "10-accessibility", len(noalt),
                  "<img> に alt が無い。情報画像は alt、装飾は alt=\"\"", noalt))

    # 7) outline 抹消で focus 不可視 — 10-accessibility「focus 必ず可視」
    no_out = lines_of(text, r'outline:\s*(?:none|0)\b')
    if no_out and not re.search(r':focus-visible', text, re.I):
        f.append((ERROR, "FOCUS-INVISIBLE", "10-accessibility", len(no_out),
                  "outline:none があり :focus-visible 代替が無い。focus を必ず可視化", no_out))

    # 8) 見出しレベル飛び — components/display「h1〜h6 を飛ばさない」
    levels = [(int(m.group(1)), text.count("\n", 0, m.start()) + 1)
              for m in re.finditer(r'<h([1-6])\b', text, re.I)]
    skips = [ln for (lv, ln), (pv, _) in zip(levels[1:], levels) if lv - pv > 1]
    if skips:
        f.append((WARN, "HEADING-SKIP", "components/display", len(skips),
                  "見出しレベルを飛ばしている（例 h2→h4）。文書順で1段ずつ", skips))

    # 9) reduced-motion 欠落 — 09-motion / prohibited
    if re.search(r'@keyframes|transition:|animation:', text, re.I) and \
       not re.search(r'prefers-reduced-motion', text, re.I):
        f.append((WARN, "NO-REDUCED-MOTION", "09-motion", 1,
                  "アニメ/transition があるのに prefers-reduced-motion 対応が無い", []))

    # 10) アクセント色数 — prohibited「1ページに3色以上のアクセント」(情報)
    hues = {}
    for hx in set(re.findall(r'#[0-9a-fA-F]{6}\b', text)):
        H, S, L = hex_to_hsl(hx)
        if S >= 0.30 and 0.12 < L < 0.88:          # 彩度のある中明度＝アクセント候補
            hues.setdefault(round(H / 30) * 30, set()).add(hx.lower())
    if len(hues) > 4:                               # 1アクセント + semantic(最大4) = 5 まで許容
        sample = ", ".join(sorted({c for s in hues.values() for c in s})[:8])
        f.append((INFO, "ACCENT-COUNT", "prohibited 色彩", len(hues),
                  f"彩度のある色相が {len(hues)}系統（{sample}…）。UIシグナルは1アクセント+semanticに"
                  "（コンテンツ画像/ロゴ/作例は対象外）", []))

    return f

def main(argv):
    files = []
    for a in (argv or ["examples/benchmark/*.html"]):
        files += sorted(glob.glob(a))
    if not files:
        print("no files matched", file=sys.stderr); return 2
    total_err = 0
    order = {ERROR: 0, WARN: 1, INFO: 2}
    for path in files:
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError as e:
            print(f"!! {path}: {e}"); continue
        findings = sorted(check(text), key=lambda x: order[x[0]])
        errs = sum(1 for fi in findings if fi[0] == ERROR)
        warns = sum(1 for fi in findings if fi[0] == WARN)
        total_err += errs
        head = f"\n=== {path}  ({errs} error, {warns} warn) ==="
        print(head if findings else f"\n=== {path}  ✓ clean ===")
        for sev, rule, src, n, hint, lns in findings:
            loc = ("  @ " + ",".join(map(str, lns[:8])) + ("…" if len(lns) > 8 else "")) if lns else ""
            print(f"  [{sev:5}] {rule:18} x{n:<3} ({src})\n           {hint}{loc}")
    print(f"\n--- {len(files)} file(s), {total_err} error(s) total ---")
    return min(total_err, 100)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
