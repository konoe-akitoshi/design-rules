#!/usr/bin/env python3
"""
install-skills — このリポジトリのスキルを ~/.claude/skills/ へインストールする。

スキルは guidelines/・tokens.json・prohibited.md（このリポジトリが SSOT）を
`${CLAUDE_SKILL_DIR}/../../../` 相対で参照している。個人スキルディレクトリに
置くとこの相対参照が壊れるため、コピー時に**このリポジトリの絶対パス**へ
書き換える。知識の実体はリポジトリ側に残るので二重管理にならない。

使い方:
  python tools/install-skills.py          # インストール/更新
  python tools/install-skills.py --check  # 差分確認のみ（書き込みなし）

リポジトリを移動/リネームしたら再実行すること。
"""
import sys, shutil, filecmp
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / ".claude" / "skills"
DST = Path.home() / ".claude" / "skills"
REPO_POSIX = REPO.as_posix()  # C:/Users/... 形式（スラッシュ）

REWRITES = [
    ("${CLAUDE_SKILL_DIR}/../../..", REPO_POSIX),  # パス変数参照
    ("](../../../", f"]({REPO_POSIX}/"),           # Markdown リンク
]


def rewrite(text: str) -> str:
    for old, new in REWRITES:
        text = text.replace(old, new)
    return text


def main(argv):
    check_only = "--check" in argv
    if not SRC.is_dir():
        print(f"skills dir not found: {SRC}", file=sys.stderr)
        return 2

    changed = 0
    for skill_dir in sorted(p for p in SRC.iterdir() if p.is_dir()):
        dst_dir = DST / skill_dir.name
        for src_file in skill_dir.rglob("*"):
            if not src_file.is_file():
                continue
            rel = src_file.relative_to(skill_dir)
            dst_file = dst_dir / rel
            if src_file.suffix in (".md", ".txt", ".json"):
                content = rewrite(src_file.read_text(encoding="utf-8"))
                up_to_date = dst_file.is_file() and dst_file.read_text(encoding="utf-8") == content
                if not up_to_date:
                    changed += 1
                    print(("would update: " if check_only else "installed: ") + str(dst_file))
                    if not check_only:
                        dst_file.parent.mkdir(parents=True, exist_ok=True)
                        dst_file.write_text(content, encoding="utf-8", newline="\n")
            else:
                up_to_date = dst_file.is_file() and filecmp.cmp(src_file, dst_file, shallow=False)
                if not up_to_date:
                    changed += 1
                    print(("would copy: " if check_only else "copied: ") + str(dst_file))
                    if not check_only:
                        dst_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(src_file, dst_file)

    print(f"\n{'check' if check_only else 'install'} done — {changed} file(s) "
          f"{'need update' if check_only else 'updated'}, target: {DST}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
