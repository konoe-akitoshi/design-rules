# Color System（配色システム — 実装値）

このリポジトリの思想・原則を、**実際に実装できる色の値**へ落としたもの。
これまで配色は「青＝信頼」「text-black禁止」のような*意味・原則*しか無く、具体的なパレットが存在しなかった。このファイルがその欠落を埋める。

機械可読版は [tokens.json](../../tokens.json) の `color`。値はそちらを正とする。

## 導出根拠（推測ではなく思想から導く）

| 決定 | 由来 |
|------|------|
| `text-black` を使わず ink = slate系の濃色 | Rams 抑制（VIS-03） |
| アクセントは **1色＋セマンティック**のみ | Calm（IX-10） |
| アクセント = **青** | colorPsychology「青＝安心・信頼・SaaS/管理画面」 |
| 低彩度・ヘアライン中心、影でなく境界線 | Rams / Tufte（data-ink）/ Linear（静かなUI） |
| 状態を**色だけで伝えない**（アイコン/ラベル併用） | WCAG 1.4.1 / Apple HIG（IX-15） |
| コントラスト比 本文4.5:1・UI3:1 | tokens.json `wcag` |

---

## パレット

> コントラストは白(#FFFFFF)地・概算。`本文可` = 通常テキスト 4.5:1以上 / `UI/大のみ` = 3:1以上（小さい本文には使わない）。実装時に最終検証すること。

### ニュートラル（slate ramp）

| トークン | hex | 役割 | コントラスト(対白) |
|---------|-----|------|------------------|
| `--c-canvas` | `#F3F5F8` | アプリ背景（最背面） | — |
| `--c-surface` | `#FFFFFF` | パネル・カード面 | — |
| `--c-sunk` | `#EEF1F4` | 沈んだ面・トラック・hover地 | — |
| `--c-line` | `#DDE3E9` | ヘアライン境界 | UI部品(3:1)用 |
| `--c-line-strong` | `#C4CCD5` | 強い境界・区切り | UI部品 |
| `--c-quiet` | `#8A93A0` | 三次テキスト・ラベル・mono | **UI/大のみ**（本文不可） |
| `--c-muted` | `#586170` | 二次テキスト・説明文 | 本文可 (≈5.6:1) |
| `--c-ink-soft` | `#2A313C` | 見出し副次 | 本文可 |
| `--c-ink` | `#14181F` | 主要テキスト（黒の代替） | 本文可 (≈16:1) |

### アクセント（青・プライマリ1色）

| トークン | hex | 役割 | コントラスト |
|---------|-----|------|------|
| `--c-accent` | `#2348C6` | 主要操作・リンク・現在状態(active) | 本文可 (≈6.5:1) |
| `--c-accent-ink` | `#1B3AA8` | hover/押下（濃い） | 本文可 |
| `--c-accent-sunk` | `#EAEEFB` | 選択中の淡い地・タグ地 | — |
| `--c-on-accent` | `#FFFFFF` | アクセント上の文字 | 対accent 6.5:1 |

### セマンティック（深く静かに。蛍光色にしない）

各色は `text`（文字/アイコン）/ `bg`（淡い地）/ `border` の3役割。

| 意味 | text | bg | border | 用途 |
|------|------|----|--------|------|
| success | `#197A4B` | `#E7F4EC` | `#B7DCC6` | 完了・正常・安全 |
| warning | `#9A6300` | `#FBF1DE` | `#ECD3A3` | 確認中・注意 |
| danger | `#B5302A` | `#FBEAE8` | `#ECC2BE` | エラー・削除・危険 |
| info | `#2348C6` | `#EAEEFB` | `#C8D4F5` | 情報（accentと共用） |

---

## CSS変数（コピーして使う）

```css
:root {
  /* neutral */
  --c-canvas:      #F3F5F8;
  --c-surface:     #FFFFFF;
  --c-sunk:        #EEF1F4;
  --c-line:        #DDE3E9;
  --c-line-strong: #C4CCD5;
  --c-quiet:       #8A93A0;  /* 本文に使わない（3:1） */
  --c-muted:       #586170;
  --c-ink-soft:    #2A313C;
  --c-ink:         #14181F;  /* text-black の代わり */

  /* accent (primary 1色) */
  --c-accent:      #2348C6;
  --c-accent-ink:  #1B3AA8;
  --c-accent-sunk: #EAEEFB;
  --c-on-accent:   #FFFFFF;

  /* semantic */
  --c-success: #197A4B; --c-success-bg: #E7F4EC; --c-success-border: #B7DCC6;
  --c-warning: #9A6300; --c-warning-bg: #FBF1DE; --c-warning-border: #ECD3A3;
  --c-danger:  #B5302A; --c-danger-bg:  #FBEAE8; --c-danger-border:  #ECC2BE;
  --c-info:    #2348C6; --c-info-bg:    #EAEEFB; --c-info-border:    #C8D4F5;
}
```

---

## 役割マッピング（どこに何を使うか）

| 場所 | トークン |
|------|---------|
| ページ背景 | `--c-canvas` |
| カード・パネル | `--c-surface` |
| 境界線（影の代わり） | `--c-line`（通常）/ `--c-line-strong`（強調） |
| 見出し | `--c-ink` |
| 本文 | `--c-ink` / 説明は `--c-muted` |
| ラベル・補助・mono | `--c-quiet` |
| 主要ボタン・リンク・現在地 | `--c-accent`（hover時 `--c-accent-ink`） |
| 選択中の項目地 | `--c-accent-sunk` |
| 成功/注意/危険/情報 | セマンティック3役割 |

## 状態（state）規約

| 状態 | 表現 |
|------|------|
| hover | 面: `surface→sunk` / アクセント: `accent→accent-ink` |
| active/選択中 | 地 `accent-sunk` ＋ 文字 `accent` ＋ 境界 `line` |
| disabled | 文字 `quiet` ＋ 地 `sunk`。彩度を上げない |
| focus | `outline: 2px solid var(--c-accent); outline-offset: 1px`（必ず可視） |

## Do / Don't

- ✅ 影の代わりにヘアライン境界（`--c-line`）で面を分ける
- ✅ アクセントは「主要操作・現在状態」にだけ使う。多用しない
- ✅ 状態は色＋アイコン/ラベルで二重化（色覚多様性・WCAG 1.4.1）
- ❌ `#000` / `text-black` 直接使用 → `--c-ink`
- ❌ 1画面にアクセントを3箇所以上の*意味*で散らす → プライマリ1色＋セマンティック
- ❌ `--c-quiet` を小さい本文に使う（コントラスト不足）
- ❌ グラデーション地・強い影で面を持ち上げる（Rams違反）

## トレーサビリティ

根拠章: 07 restraint-form（抑制）/ 03 interaction-feedback（注意の階層）/ 02 information-structure（視覚分類=重要度）/ 10 accessibility（色だけで伝えない）。
思想: Dieter Rams（抑制）/ Calm Technology（注意の階層）/ Tufte（data-ink）。
