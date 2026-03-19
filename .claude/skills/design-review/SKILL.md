---
name: design-review
description: HTML/JSXコードをデザインルールに照らしてレビューする。禁止パターン違反、トークン未使用、非対称パディング不備、WCAG違反を検出し修正案を出力する。
disable-model-invocation: true
argument-hint: "[ファイルパス or コードスニペット]"
allowed-tools: Read, Grep, Glob
---

# Design Review

指定されたファイルまたはコードを、このリポジトリのデザインルールに照らしてレビューする。

## 参照するルール

以下のファイルを読み込んで、レビュー基準とすること:

1. `${CLAUDE_SKILL_DIR}/../../../prohibited.md` — 禁止パターン一覧
2. `${CLAUDE_SKILL_DIR}/../../../tokens.json` — デザイントークン定義
3. `${CLAUDE_SKILL_DIR}/../../../CLAUDE.md` — クイックリファレンス

## レビュー対象

$ARGUMENTS

## チェック項目

以下の順序でチェックし、違反を検出すること:

### 1. 禁止パターン違反
prohibited.md に定義された禁止パターンとの照合:
- `shadow-lg`, `shadow-xl` の使用
- `text-black` の使用
- カラーバー（`border-t-4`, `border-l-4` + カラー）
- グラデーション背景の多用
- 絵文字の過剰使用
- ハードコードされた色（`bg-blue-500` 等、トークン外の色指定）

### 2. スペーシング違反
- 4の倍数以外のスペーシング値
- 対称パディング（`p-4` 単独でのカード/ボタン等）→ 非対称（`py-4 px-6`）推奨
- Visual Rhythm の欠如（全要素が同じ margin-bottom）

### 3. 角丸違反
- 黄金比階層（16/10/6/4/2px）外の値
- 子要素の角丸 ≥ 親要素の角丸
- `rounded-full` の装飾的乱用

### 4. タッチターゲット違反
- インタラクティブ要素の 48px 未満
- タッチターゲット間隔 8px 未満
- モバイルでの CTA 配置位置

### 5. WCAG / アクセシビリティ
- コントラスト比の懸念（明るい背景 + 薄い文字色等）
- 色のみで状態を表現している箇所

## 出力フォーマット

以下の形式で出力すること:

```
## Design Review 結果

### 違反サマリー
- Critical: X件
- Warning: Y件
- Info: Z件

### 違反詳細

#### [Critical] 禁止パターン: shadow-lg
- 箇所: ファイル名:行番号
- 現在: `shadow-lg`
- 修正: `shadow-sm`

#### [Warning] 非対称パディング未適用
- 箇所: ファイル名:行番号
- 現在: `p-4`
- 修正: `py-4 px-6`（カード要素の場合）

...
```

重大度の基準:
- **Critical**: 禁止パターン違反、WCAG違反
- **Warning**: トークン未使用、非対称パディング不備
- **Info**: より良い代替パターンの提案
