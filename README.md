# Design System Documentation

Blog Design System based on theoretical foundations and practical implementation.

## 📋 Documentation Structure

### Core Design Theories
- **[Visual Layout](./visual-layout.md)** - ゲシュタルトの法則、黄金比、三分割法、視覚階層
- **[Color Theory](./color-theory.md)** - 色相環、配色システム、色彩心理
- **[UI/UX Laws](./ui-ux-laws.md)** - ヤコブの法則、ヒックの法則、認知効果
- **[Dieter Rams Principles](./dieter-rams.md)** - 良いデザイン10ヶ条

### Implementation Systems
- **[Spacing System](./spacing-system.md)** - 4pt/8ptグリッド、階層的余白設計
- **[Border Radius](./border-radius.md)** - 黄金比相対角丸、階層的調和システム
- **[Responsive Design](./responsive-design.md)** - 流動的グリッド、柔軟な画像、メディアクエリ

## 🎯 Quick Implementation Guide

### Essential Rules
```css
/* 4pt/8pt Grid System */
--spacing-1: 0.25rem;    /* 4px */
--spacing-2: 0.5rem;     /* 8px */
--spacing-4: 1rem;       /* 16px */
--spacing-8: 2rem;       /* 32px */

/* Golden Ratio Border Radius (推奨) */
--radius-golden-0: 1rem;      /* 16px - Level 0 */
--radius-golden-1: 0.625rem;  /* 10px - Level 1 */
--radius-golden-2: 0.375rem;  /* 6px - Level 2 */
--radius-golden-3: 0.25rem;   /* 4px - Level 3 */

/* Golden Ratio + Visual Correction Rule */
childRadius = parentRadius × 0.618 × 0.75 (錯視補正)
theoreticalValue ≠ visuallyCorrectValue
```

### Component Patterns
- **Cards**: `rounded-golden-0` (16px) → content `rounded-corrected` (8px)
- **Images**: Golden ratio + visual correction for natural appearance
- **Buttons**: `rounded-corrected` (4px) for optimal visual balance
- **Spacing**: Internal padding ≤ External margin
- **Hierarchy**: Each level = parent × 0.618 × 0.75 (錯視補正適用)
- **Visual Testing**: 数値的正確性より視覚的調和を優先

## 📖 Usage in Development

When implementing components:
1. **Read relevant theory files** for understanding
2. **Apply core rules** from quick guide
3. **Follow existing patterns** in codebase
4. **Test responsive behavior** on multiple devices

## 🔄 Maintenance

This documentation should be updated when:
- New design patterns are established
- Existing rules are refined
- Component library is extended
- User feedback suggests improvements