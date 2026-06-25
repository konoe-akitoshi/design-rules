# Design Rules — AI Design System Guide

このリポジトリはUI設計の理論・原則・実装システムをまとめたデザインルール集です。
UI生成時は、このファイルのクイックリファレンスを参照し、tokens.json の値を使用してください。

## 設計哲学

- **コンテンツファースト**: 装飾ではなく情報を伝えるデザイン
- **システム思考**: 複雑なシステムを人間が理解・操作・制御できる形に翻訳する
- **情報空間設計**: 複雑なシステムを理解可能な構造に変換する
- **可能な限りデザインを抑制する**: ディーター・ラムスの第10原則
- **数値的正確性 ≠ 視覚的正確性**: 人間の知覚に合わせた錯視補正を行う

デザインの正は [guidelines/](./guidelines/README.md)（自己完結したデザインガイドライン）。AIへの対応は [prohibited.md](./prohibited.md) 等の別レイヤー。原典（集めた思想）は `memo/` にアーカイブ。

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
| レイアウトを組む | `guidelines/04-layout-space.md` + `guidelines/values/spacing-system.md` |
| ボタンを作る | `guidelines/values/border-radius.md`（角丸）+ `guidelines/04-layout-space.md`（錯視補正） |
| カードUIを作る | `guidelines/values/spacing-system.md`（非対称padding）+ `guidelines/values/border-radius.md`（入れ子角丸） |
| フォームを作る | `guidelines/values/spacing-system.md` + `guidelines/values/responsive-mobile.md`（タッチターゲット） |
| モバイル対応する | `guidelines/values/responsive-mobile.md` |
| 配色を決める | `guidelines/05-color.md` + `guidelines/values/color-system.md`（実値） |
| アイコンを配置する | `guidelines/04-layout-space.md`（重心補正・オーバーシュート） |
| 設計姿勢・原則・題材から構造 | `guidelines/01-foundations.md` |
| ジャンル判別（A/B）・全体像・決定順 | `guidelines/README.md` |
| ルールが矛盾したとき | `guidelines/README.md` の「優先順位」 |

原典（集めた思想の散文）は `memo/` にアーカイブ。通常は `guidelines/` だけで足りる。

---

## スキル（スラッシュコマンド）

各スキルは [guidelines/](./guidelines/README.md) の該当章を判断基準として読む。ワークフローの段ごとに発火する。

| 段 | コマンド | 用途 |
|----|---------|------|
| 着手前 | `/design-requirements-grill [説明]` | 要件をガイドライン決定順で問い詰めて明確化。曖昧なまま実装に入らせない |
| 要件定義 | `/ux-strategist [説明]` | 観測→判断→制御→FB・認知労働・介入点を設計戦略に落とす |
| 生成 | `/design-apply [UIの説明]` | ガイドライン/トークン準拠でUIコードを生成。セルフチェック付き |
| 設計 | `/composition-patterns [説明]` | 繰り返す構造を再利用可能なパターン（signifier・5状態内包）へ |
| ポリッシュ | `/baseline-ui [ファイル]` | スペーシング・タイポ・錯視補正をガイドラインに沿って仕上げ |
| a11y | `/fixing-accessibility [ファイル]` | コントラスト・色のみ依存・ターゲット・focus・ラベルを修正 |
| アニメ後 | `/fixing-motion-performance [ファイル]` | 装飾アニメ除去・意味ある動きへ・reduced-motion付与 |
| QAゲート | `/web-design-guidelines [ファイル]` | 原則レベル検査（情報構造・操作・抑制・状態・a11y）を根拠付きで |
| 検証 | `/design-review [ファイル]` | 機械的チェック（禁止パターン・トークン・非対称padding・WCAG） |
| 参照 | `/design-tokens [カテゴリ]` | トークン値のクイック参照 |

`/frontend-design`（美的方向）と React パフォーマンスは既存スキルを利用する。

---

## トークン参照

具体的な値は `tokens.json` を正とする。SSOT（Single Source of Truth）として全トークンが定義されている。

---

## アーキテクチャ — デザイン と AI対応 を分ける

- **`guidelines/`** … **自己完結したデザインガイドライン**。思想→使うための理論→使える規則の3層 ＋ `values/color-system.md` / `values/spacing-system.md` / `values/border-radius.md` / `values/responsive-mobile.md` を内包。値の正は `tokens.json`。**デザインはこれで完結する**。
- **`prohibited.md`（＋今後の同種ファイル）** … **AIへの対応**（AI生成が外しがちな点の禁止形）。デザインとは別レイヤーとして育てる。
- **`.claude/skills/`** … 上記を使ってページ/UIを実際に作る・直す・検証する道具。

UI を作る/直す/検証するときは、`guidelines/README.md` の**決定順**（目的→構造→操作→レイアウト→造形→抑制→検証）と **A/B判別**（ブランド系は A だけ、道具は A+B）に従い、見た目から始めない。`guidelines/01-foundations.md` の「**題材から構造を導く・テンプレ骨格禁止**」を必ず通す。値は `tokens.json` / `guidelines/values/color-system.md`。`prohibited.md` を併せてセルフチェック。

原典（集めた思想・原則・理論の散文）は `memo/` にアーカイブ（通常は不要）。
