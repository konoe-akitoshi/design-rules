# Design Rules

デザインシステムドキュメント。理論的基盤と実装ガイドライン。
人間とAIの両方が参照できる設計。

## 構成

```
CLAUDE.md           AIエントリーポイント（クイックリファレンス + タスクベースガイド）
tokens.json         デザイントークンのSSOT（機械可読）
prohibited.md       禁止パターン一覧
principles/         原則・哲学
theory/             理論
systems/            実装システム
```

## AI向け：使い方

1. `CLAUDE.md` を読む — 基本的なUI生成はこれだけで完結
2. 具体的な値は `tokens.json` を参照（SSOT）
3. `prohibited.md` で禁止パターンを確認
4. 詳細が必要な場合は `CLAUDE.md` のタスクベースガイドに従って個別ドキュメントを読む

## ドキュメント一覧

### AI向け

| ファイル | 内容 |
|----------|------|
| [CLAUDE.md](./CLAUDE.md) | AIエントリーポイント。クイックリファレンス + タスクベース読み込みガイド |
| [tokens.json](./tokens.json) | デザイントークン定義（スペーシング・角丸・タッチターゲット・WCAG等） |
| [prohibited.md](./prohibited.md) | 禁止パターン一覧（AI生成パターン排除含む） |

### Principles（原則）

| ファイル | 内容 |
|----------|------|
| [design-principles.md](./principles/design-principles.md) | ディーター・ラムス10原則、UI/UX Laws |

### Theory（理論）

| ファイル | 内容 |
|----------|------|
| [visual-design.md](./theory/visual-design.md) | ゲシュタルト、黄金比、色彩理論、WCAG |
| [optical-adjustment.md](./theory/optical-adjustment.md) | 錯視補正、重心補正、オーバーシュート |

### Systems（実装）

| ファイル | 内容 |
|----------|------|
| [spacing-system.md](./systems/spacing-system.md) | 4pt/8ptグリッド、非対称パディング、Optical Spacing |
| [border-radius.md](./systems/border-radius.md) | Squircle、黄金比角丸、錯視補正システム |
| [responsive-mobile.md](./systems/responsive-mobile.md) | レスポンシブ3原則、Fitt's Law、タッチターゲット |

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
