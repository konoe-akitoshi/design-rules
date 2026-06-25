# Design Rules

デザインシステムドキュメント。理論的基盤と実装ガイドライン。
人間とAIの両方が参照できる設計。

## 構成

```
CLAUDE.md           AIエントリーポイント（クイックリファレンス + タスクベースガイド）
guidelines/         デザインガイドライン（自己完結）— 思想→理論→規則の3層 + 実装(spacing/radius/responsive/color-system)
tokens.json         デザイントークンのSSOT（機械可読・量）
prohibited.md       AIへの対応（AI生成が外しがちな点の禁止形）— デザインとは別レイヤー
.claude/skills/     ステージ別スキル群（guidelines + prohibited を使って製作・検証）
examples/           デモHTML
memo/               原典アーカイブ（集めた思想・原則・理論。通常は参照不要）
```

## AI向け：使い方

1. `CLAUDE.md` を読む — エントリーポイント
2. デザインは `guidelines/`（自己完結したデザインガイドライン）に従う。値は `tokens.json`
3. `prohibited.md`（AIへの対応）で禁止パターンを確認
4. 原典の散文が要るときだけ `memo/` を見る

## ドキュメント一覧

### デザインガイドライン（自己完結）— `guidelines/`

| ファイル | 内容 |
|----------|------|
| [README.md](./guidelines/README.md) | 適用範囲(A:一般 / B:道具レンズ)・3層の書き方・章構成・決定順・優先順位 |
| 01-foundations 〜 10-accessibility | 思想→使うための理論→使える規則の10章（[索引](./guidelines/README.md)） |
| [values/color-system.md](./guidelines/values/color-system.md) | 配色の実値（パレット・役割・状態・CSS変数） |
| [values/spacing-system.md](./guidelines/values/spacing-system.md) | 4pt/8ptグリッド・非対称padding・Optical Spacing |
| [values/border-radius.md](./guidelines/values/border-radius.md) | Squircle・黄金比角丸・錯視補正 |
| [values/responsive-mobile.md](./guidelines/values/responsive-mobile.md) | レスポンシブ・Fitt's Law・タッチターゲット |

### 値・AIへの対応

| ファイル | 内容 |
|----------|------|
| [tokens.json](./tokens.json) | デザイントークン（量のSSOT） |
| [prohibited.md](./prohibited.md) | AIへの対応（AI生成パターンの禁止形）。デザインとは別レイヤー |

### スキル — `.claude/skills/`

着手前 `grill` / 戦略 `ux-strategist` / 生成 `design-apply` / 設計 `composition-patterns` / 仕上げ `baseline-ui` / a11y `fixing-accessibility` / アニメ `fixing-motion-performance` / QA `web-design-guidelines` / 検証 `design-review` / 参照 `design-tokens`。詳細は [CLAUDE.md](./CLAUDE.md)。

### Examples（ガイドライン適用例）

| ファイル | 内容 |
|----------|------|
| [nagare-instruments.html](./examples/nagare-instruments.html) | 架空企業サイト。題材＝精密計器の「実測図」として構造を導いた版（テンプレ骨格を使わない） |
| [service-monitor.html](./examples/service-monitor.html) | 道具UI。観測→判断→制御→フィードバックの制御コンソール |
| [knowledge-workspace.html](./examples/knowledge-workspace.html) | 知識ワークスペース |

### 原典アーカイブ — `memo/`

集めた思想・原則・理論（`philosophy/` `principles/` `theory/`）と検証 `analysis.md`。guidelines/ の出典。通常は参照不要。

## クイックリファレンス

### Spacing（4pt/8pt Grid）
```css
--spacing-1: 0.25rem;    /* 4px */
--spacing-2: 0.5rem;     /* 8px */
--spacing-4: 1rem;       /* 16px */
--spacing-8: 2rem;       /* 32px */
```

### Border Radius（黄金比）
```css
--radius-golden-0: 1rem;      /* 16px - Level 0 */
--radius-golden-1: 0.625rem;  /* 10px - Level 1 */
--radius-golden-2: 0.375rem;  /* 6px - Level 2 */
--radius-golden-3: 0.25rem;   /* 4px - Level 3 */
```

### 錯視補正
```
childRadius = parentRadius × 0.618 × 0.75
theoreticalValue ≠ visuallyCorrectValue
```

### Touch Targets
```
主要操作: 48dp/pt (約9mm)
二次操作: 44dp/pt (約7-9mm)
間隔: 最小8px
```
