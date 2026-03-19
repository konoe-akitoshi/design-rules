# Design Rules — AI Design System Guide

このリポジトリはUI設計の理論・原則・実装システムをまとめたデザインルール集です。
UI生成時は、このファイルのクイックリファレンスを参照し、tokens.json の値を使用してください。

## 設計哲学

- **コンテンツファースト**: 装飾ではなく情報を伝えるデザイン
- **可能な限りデザインを抑制する**: ディーター・ラムスの第10原則
- **数値的正確性 ≠ 視覚的正確性**: 人間の知覚に合わせた錯視補正を行う

---

## クイックリファレンス — スペーシング（4pt/8pt Grid）

| トークン | 値 | Tailwind | 用途 |
|---------|------|---------|------|
| spacing-1 | 4px | `p-1` `m-1` `gap-1` | 基本単位・要素内余白 |
| spacing-2 | 8px | `p-2` `m-2` `gap-2` | 要素内余白・標準間隔 |
| spacing-3 | 12px | `p-3` `m-3` `gap-3` | コンパクトな要素間余白 |
| spacing-4 | 16px | `p-4` `m-4` `gap-4` | 要素間余白 |
| spacing-6 | 24px | `p-6` `m-6` `gap-6` | カード内横パディング |
| spacing-8 | 32px | `p-8` `m-8` `gap-8` | セクション間余白 |

### 非対称パディング（必須）

縦横同値の `padding: 16px` は禁止。以下の比率で非対称にする。

| 要素 | padding | 比率 | Tailwind |
|------|---------|------|----------|
| カード | `16px 24px` | 1:1.5 | `py-4 px-6` |
| ボタン | `12px 20px` | 1:1.67 | `py-3 px-5` |
| バナー | `32px 48px` | 1:1.5 | `py-8 px-12` |
| タグ | `4px 12px` | 1:3 | `py-1 px-3` |
| フォーム | `8px 16px` | 1:2 | `py-2 px-4` |

---

## クイックリファレンス — 角丸（黄金比システム）

| Level | 値 | Tailwind | 用途 |
|-------|------|---------|------|
| 0 | 16px | `rounded-2xl` | モーダル・メインパネル |
| 1 | 10px | `rounded-lg` | カードコンテンツ・セクション |
| 2 | 6px | `rounded-md` | ボタン・画像・フォーム |
| 3 | 4px | `rounded` | タグ・バッジ |
| 4 | 2px | `rounded-sm` | 装飾要素 |

### 入れ子の角丸ルール

```
R_inner = R_outer - Padding（最小2px）
親 > 子 > 孫 の関係を必ず保持
```

---

## クイックリファレンス — 錯視補正

| 対象 | 補正 |
|------|------|
| 三角形アイコン（▶等） | 尖端方向へ H/6（約16.7%）オフセット |
| 円形アイコン | 正方形より 3〜5% 拡大 |
| ボタンテキスト | `translateY(-1px)` で上方向補正 |
| 太字テキスト下余白 | 標準値 × 0.75 |
| 軽いテキスト下余白 | 標準値 × 1.25 |

---

## クイックリファレンス — タッチターゲット

| 要素 | 最小サイズ | 最小間隔 |
|------|-----------|---------|
| 主要操作（FAB・完了等） | 48px × 48px | 8px |
| 二次操作（設定等） | 44px × 44px | 8px |
| アイコンボタン | 視覚24px + padding12px = 48px | 8px |

モバイルでは主要CTAを画面下部（親指ゾーン）に配置。`env(safe-area-inset-*)` を必ず適用。

---

## クイックリファレンス — WCAG コントラスト

| 対象 | 最小比率 |
|------|---------|
| 通常テキスト | 4.5:1 |
| 大きな文字（18px以上 or 太字） | 3:1 |
| アイコン・UI部品 | 3:1 |

色だけで状態を伝えない。アイコン・ラベルを必ず併用する。

---

## 禁止パターン（重要）

詳細は [prohibited.md](./prohibited.md) を参照。特に注意すべき項目:

- `shadow-lg`, `shadow-xl` → `shadow-sm` を使う
- `text-black` → `text-slate-900` を使う
- カラーバー（`border-t-4`） → 全周ボーダーまたは装飾なし
- グラデーション多用 → ソリッドカラー基本
- 絵文字多用 → 必要最小限。SVGアイコン推奨
- 均等padding → 非対称padding必須
- 1ページ3色以上のアクセント → プライマリ1色 + セマンティック

---

## タスクベース読み込みガイド

必要に応じて詳細ドキュメントを読み込むこと。

| タスク | 参照ファイル |
|-------|------------|
| レイアウトを組む | `systems/spacing-system.md` + `theory/visual-design.md` |
| ボタンを作る | `systems/border-radius.md`（角丸）+ `theory/optical-adjustment.md`（テキスト補正） |
| カードUIを作る | `systems/spacing-system.md`（非対称padding）+ `systems/border-radius.md`（入れ子角丸） |
| フォームを作る | `systems/spacing-system.md` + `systems/responsive-mobile.md`（タッチターゲット） |
| モバイル対応する | `systems/responsive-mobile.md` |
| 配色を決める | `theory/visual-design.md`（色彩理論・WCAG） |
| アイコンを配置する | `theory/optical-adjustment.md`（重心補正・オーバーシュート） |
| デザイン原則を確認する | `principles/design-principles.md` |

---

## トークン参照

具体的な値は `tokens.json` を正とする。SSOT（Single Source of Truth）として全トークンが定義されている。
