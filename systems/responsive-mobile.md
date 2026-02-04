# Responsive & Mobile Design

レスポンシブデザインとモバイルタッチターゲット設計。

## 目次

1. [Responsive Design Theory](#responsive-design-theory)
2. [Mobile Touch Targets](#mobile-touch-targets)

---

## Responsive Design Theory

レスポンシブデザインの3つの基本原則。

### Ethan Marcotteの3原則

#### 1. Fluid Grid (流動的グリッド)
```css
/* 固定幅の代わりに相対単位を使用 */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.grid-item {
  width: calc(50% - 1rem); /* 固定値ではなく計算値 */
}
```

#### 2. Flexible Images (柔軟な画像)
```css
img {
  max-width: 100%;
  height: auto;
}

/* Next.js Image component */
<Image
  src={src}
  alt={alt}
  fill
  className="object-cover"
/>
```

#### 3. Media Queries (メディアクエリ)
```css
/* Mobile First アプローチ */
.element {
  /* mobile styles */
}

@media (min-width: 768px) {
  .element {
    /* tablet styles */
  }
}

@media (min-width: 1024px) {
  .element {
    /* desktop styles */
  }
}
```

### Tailwind実装

#### ブレークポイント
- `sm:` = 640px以上
- `md:` = 768px以上
- `lg:` = 1024px以上
- `xl:` = 1280px以上

#### レスポンシブパターン
```jsx
<div className="flex flex-col md:flex-row">
  <div className="w-full md:w-2/3">Content</div>
  <div className="w-full md:w-1/3">Sidebar</div>
</div>
```

---

## Mobile Touch Targets

人間工学とFitt's Lawに基づくモバイル端末対応のタッチ領域設計

### Fitt's Lawと操作性の方程式

#### フィッツの法則（Fitt's Law）

人間工学およびHCI（Human-Computer Interaction）における基本法則であり、**ターゲットに到達するまでの時間は「ターゲットまでの距離」と「ターゲットの大きさ」の関数である**とします。

**数式：**

$$
T = a + b \log_2 \left( \frac{D}{W} + 1 \right)
$$

ここで：
- `T`: 動作完了までの時間（Time）
- `D`: 開始地点からターゲット中心までの距離（Distance）
- `W`: ターゲットの幅（Width、動作方向の大きさ）
- `a, b`: 固有の係数（デバイスや操作方法に依存）

#### UIデザインへの論理的結論

この数式が示唆する2つの重要な原則：

1. **ターゲットは大きくあれ**
   - `W` が大きければ大きいほど、操作時間 `T`（およびエラー率）は減少する
   - 特に頻繁に行う操作ほど大きくする必要がある

2. **距離は短くあれ**
   - `D` を小さくする、つまり指の現在位置（多くの場合は画面下部）に近い場所に操作要素を配置すべき

#### 無限の幅の法則（Screen Edge Advantage）

画面の端（エッジ）や四隅（コーナー）は、カーソルや指がそれ以上進まない物理的な壁があるため、実質的に **W → ∞** とみなせます。

**結論: 画面端に配置されたボタンは極めて操作しやすい**

```
画面中央のボタン: W = 48px
画面端のボタン: W = ∞（実質的に）
```

### タッチターゲットの物理的サイズ基準

#### 人間の指の接触面積

人間の指の腹（Finger Pad）が画面に接触する面積は、個人差があるものの：

- **平均**: 10mm〜14mm 程度
- **指先のみ**: 8mm〜10mm 程度
- **親指**: 10mm〜12mm（人差し指より太い）

#### プラットフォーム別ガイドライン比較

主要なガイドラインにおける推奨値：

| ガイドライン | 基準単位 | 最小サイズ | 物理サイズ換算（目安） | 備考 |
|------------|---------|-----------|------------------|------|
| **Apple (iOS HIG)** | pt (ポイント) | 44 × 44 pt | 約 7mm - 9mm | 一般的なRetinaディスプレイ基準 |
| **Google (Material 3)** | dp (密度非依存画素) | 48 × 48 dp | 約 9mm | アクセシビリティ重視 |
| **WCAG 2.5.5 (AAA)** | CSS px | 44 × 44 px | デバイス依存 | 厳格なアクセシビリティ基準 |
| **WCAG 2.5.8 (AA)** | CSS px | 24 × 24 px | デバイス依存 | ターゲット間隔が十分ある場合のみ許容 |

#### 統合ルールの策定

**論理的ガイドライン：**

1. **プライマリ操作基準**
   - ナビゲーションバー、FAB、完了ボタンなどの主要要素
   - **最小 48dp/pt（約9mm）以上**のタッチ領域を確保

2. **セカンダリ操作基準**
   - リストアイテムや設定トグルなど、頻度の低い操作
   - **最小 44dp/pt** を絶対に下回らない

3. **見た目と判定エリアの分離**
   - アイコン自体の視覚サイズが24pxであっても、クリック/タップ可能なパディング（Hit Area Padding）を含めて48pxのボックスを形成

#### 見た目とタッチエリアの分離実装

```css
/* アイコンボタン: 視覚サイズ24px、タッチエリア48px */
.icon-button {
  /* 視覚的なアイコンサイズ */
  width: 24px;
  height: 24px;

  /* タッチエリアを拡張するパディング */
  padding: 12px; /* (48 - 24) / 2 = 12px */

  /* 実質的なタッチエリア: 48px × 48px */
}

/* または疑似要素で拡張 */
.icon-button-alt {
  position: relative;
  width: 24px;
  height: 24px;
}

.icon-button-alt::before {
  content: '';
  position: absolute;
  top: -12px;
  left: -12px;
  right: -12px;
  bottom: -12px;
  /* 透明な48pxのタッチエリア */
}
```

#### タッチターゲット間隔（Spacing）

ターゲット同士が近接している場合、誤タップを防ぐために最小間隔を設けます。

**推奨間隔：**
- Google Material 3: **最小8dp**
- Apple HIG: **要素間に十分な余白**（明確な数値なし、経験的に8pt〜12pt）

```css
/* ボタングループの間隔 */
.button-group {
  display: flex;
  gap: 8px; /* 最小間隔 */
}
```

### セーフエリアとコーナーの干渉

#### ベゼルレス端末の課題

iPhone X以降のベゼルレス端末や、ディスプレイ自体の四隅が大きく丸まったAndroid端末が増加しています。これにより、画面の四隅に配置されたUI要素が物理的な画面形状によって**切り取られる（Clipping）リスク**があります。

#### セーフエリアインセット（Safe Area Insets）

OSが提供する「セーフエリアインセット」の値を利用し、コンテンツが可視領域内に収まることを保証します。

**CSS環境変数：**

```css
padding-top: env(safe-area-inset-top);
padding-right: env(safe-area-inset-right);
padding-bottom: env(safe-area-inset-bottom);
padding-left: env(safe-area-inset-left);
```

#### 実装例

```css
/* ページ全体のセーフエリア対応 */
.page-container {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

/* 固定ナビゲーションバー（下部） */
.bottom-navigation {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;

  /* セーフエリア + デザイン上のパディング */
  padding-bottom: calc(16px + env(safe-area-inset-bottom));
  padding-left: calc(16px + env(safe-area-inset-left));
  padding-right: calc(16px + env(safe-area-inset-right));
}

/* FAB（Floating Action Button）*/
.fab {
  position: fixed;
  bottom: calc(24px + env(safe-area-inset-bottom));
  right: calc(24px + env(safe-area-inset-right));
}
```

### 親指ゾーンと片手操作

#### 片手操作の重要性

スマートフォンの大型化に伴い、片手操作時に親指が届く範囲（Thumb Zone）を考慮したUI配置が重要になっています。

#### 親指ゾーンの分類

スティーブン・フーバー（Steven Hoober）の研究に基づく分類：

| ゾーン | 説明 | 到達性 | 推奨用途 |
|-------|-----|--------|----------|
| **Natural Zone（自然ゾーン）** | 画面下部中央。親指を伸ばさずに届く範囲。 | ★★★★★ | 主要操作、ナビゲーション、FAB |
| **Stretch Zone（ストレッチゾーン）** | 画面上部や端。親指を伸ばせば届く範囲。 | ★★★☆☆ | 二次的な操作、設定ボタン |
| **Hard-to-Reach Zone（到達困難ゾーン）** | 画面上部の角。両手操作が必要。 | ★☆☆☆☆ | 重要度の低い情報、装飾要素 |

#### 右手持ち vs 左手持ち

- **右手持ちユーザー**: 画面右下が最も届きやすい
- **左手持ちユーザー**: 画面左下が最も届きやすい

**対応策：**
- 主要なCTA（Call to Action）ボタンは画面下部の**中央または両端**に配置
- 左右対称のレイアウトを採用
- ユーザー設定で左右を切り替え可能にする（高度な実装）

#### 実装例

```css
/* モバイル端末向けレイアウト */
@media (max-width: 640px) {
  /* 主要操作ボタンは下部に配置 */
  .primary-cta {
    position: fixed;
    bottom: calc(24px + env(safe-area-inset-bottom));
    left: 50%;
    transform: translateX(-50%); /* 中央配置 */
    width: calc(100% - 48px);
    max-width: 400px;
    height: 56px;
  }

  /* ナビゲーションは下部に固定 */
  .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 64px;
    padding-bottom: env(safe-area-inset-bottom);
  }

  /* 重要度の低い設定ボタンは上部 */
  .settings-button {
    position: absolute;
    top: 16px;
    right: 16px;
  }
}
```

### 実装ガイドライン

#### チェックリスト

**タッチターゲット設計の必須項目：**

- [ ] すべての主要操作ボタンは最小48px × 48px以上か？
- [ ] アイコンボタンは視覚サイズが小さくてもタッチエリアは48px以上か？
- [ ] ボタン間隔は最小8px以上確保されているか？
- [ ] FABは画面下部の親指ゾーンに配置されているか？
- [ ] セーフエリアインセットが適用されているか？
- [ ] 画面端の「無限の幅の利点」を活用しているか？

#### レスポンシブ対応

```css
/* デスクトップ: 小さめのボタンでOK */
.button {
  min-width: 32px;
  min-height: 32px;
}

/* タブレット: 中間サイズ */
@media (pointer: coarse) and (min-width: 768px) {
  .button {
    min-width: 40px;
    min-height: 40px;
  }
}

/* スマートフォン: 大きなタッチエリア */
@media (pointer: coarse) and (max-width: 767px) {
  .button {
    min-width: 48px;
    min-height: 48px;
  }

  .primary-button {
    min-width: 64px;
    min-height: 56px;
  }
}
```

#### タッチデバイス検出

```css
/* pointer: coarse = タッチデバイス */
@media (pointer: coarse) {
  .interactive-element {
    min-width: 48px;
    min-height: 48px;
  }
}

/* pointer: fine = マウス・トラックパッド */
@media (pointer: fine) {
  .interactive-element {
    min-width: 32px;
    min-height: 32px;
  }
}

/* ホバー可能なデバイス */
@media (hover: hover) {
  .button:hover {
    background-color: var(--hover-bg);
  }
}
```

### まとめ：人間工学に基づいた設計

モバイルタッチターゲットの設計は、単なるピクセル値の決定ではなく、**人間の生理的特性とFitt's Lawという数学的原理の統合**です。

#### 核心原則

1. **最小サイズの厳守**
   - 主要操作: 48dp/pt (約9mm)
   - 二次的操作: 44dp/pt (約7-9mm)

2. **Fitt's Lawの活用**
   - 大きなターゲット + 短い距離 = 高速で正確な操作
   - 画面端の「無限の幅の利点」を活用

3. **親指ゾーンの最適化**
   - 主要操作は画面下部の自然ゾーンに配置
   - 重要度の低い操作は上部へ

4. **セーフエリアの尊重**
   - `env(safe-area-inset-*)` を必ず適用
   - コーナークリッピングを回避

**目的: 誤操作を最小限に抑え、快適で効率的なユーザー体験を実現する**
