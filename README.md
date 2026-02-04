# Design Rules

デザインシステムドキュメント。理論的基盤と実装ガイドライン。

## 構成

```
principles/     原則・哲学
theory/         理論
systems/        実装システム
```

## ドキュメント一覧

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
