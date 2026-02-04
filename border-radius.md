# Border Radius Design

入れ子角丸設計ルールと黄金比による相対角丸システム。

## 目次

1. [Squircleと曲率連続性の数理](#squircleと曲率連続性の数理)
2. [入れ子構造の同心円理論](#入れ子構造の同心円理論)
3. [黄金比相対角丸システム](#黄金比相対角丸システム)
4. [錯視補正システム](#錯視補正システム)
5. [実装戦略](#実装戦略)

---

## Squircleと曲率連続性の数理

### 標準的な円弧接続の限界（G1連続性）

通常のCSS `border-radius` は、長方形の角に**正円の四分の一（Quarter Circle）**を配置することで角丸を形成します。

**幾何学的特性：**
- 直線部分: 曲率 κ = 0（平坦）
- 円弧部分: 曲率 κ = 1/r（一定）
- **接続点での問題**: 曲率が 0 から 1/r へ**不連続にジャンプ**

```
直線 ────▶ 円弧
κ = 0      κ = 1/r
      ↑ 不連続点（G1連続だがG2非連続）
```

この**曲率の不連続性（G2連続性の欠如）**により：
- 人間の目には微細な「角張り」や「継ぎ目」として知覚される
- 高解像度ディスプレイ上では反射光（ハイライト）のラインが折れ曲がる
- 物理的な物体としてのリアリティや高級感を損なう

### スーパー楕円とSquircleの定義

**Squircle**は「スーパー楕円（Superellipse）」の特殊なケースであり、19世紀のフランスの数学者ガブリエル・ラメ（Gabriel Lamé）によって記述されたラメ曲線に基づいています。

**スーパー楕円の一般式：**

$$
\left| \frac{x}{a} \right|^n + \left| \frac{y}{b} \right|^n = 1
$$

ここで：
- `a`, `b`: 楕円の半軸（semi-axes）の長さ
- `n`: 形状を決定する指数パラメータ
  - n = 2: 通常の楕円（a=b なら円）
  - n > 2: 徐々に長方形に近づく
  - **n = 4**: Squircle（円と正方形の中間）

**Squircleの最大の特徴：**
- 直線部分からカーブ部分への移行において、**曲率が連続的に変化**
- 0から徐々に増加し、頂点で最大となる
- **G2連続性**を実現し、視覚的な「継ぎ目」が完全に消失

### Appleの「Continuous Corners」アプローチ

AppleはiOS 7以降、アプリアイコンやハードウェアのコーナーデザインに、単純な円弧ではなくSquircleに近い形状を採用しています。

**Appleの形状特性：**
- スーパー楕円の指数で言うところの **n ≈ 5** に近い形状
- Quintic（5次）ベジェ曲線を用いて近似
- **G3連続性**を目指し、曲率の変化率までもが滑らかに
- 角のカーブが直線部分の奥深くまで入り込み、「取って付けた」印象を与えない

### 形状タイプの分類と選択基準

| 形状タイプ | 数学的定義 | 特徴 | 視覚的効果 | 推奨用途 |
|-----------|-----------|-----|-----------|----------|
| **Simple Round** | n=2 (円弧) | 実装容易、標準CSS。曲率不連続。 | 機能的、機械的、中立的 | 入力フィールド、内部コンテナ、低コスト実装 |
| **Squircle** | n=4 | 直線とカーブの中間的張力。曲率連続（G2）。 | モダン、洗練、柔らかさ | カードUI、モーダルウィンドウ、主要な画像コンテナ |
| **Organic (Apple-like)** | n ≈ 5 | 極めて滑らか。四隅への指向性が弱い（G3連続）。 | 有機的、親密、象徴的 | アプリアイコン、ブランドロゴ、FAB |

**ガイドライン指針：**
- **n=4（Squircle）** を基本形状として推奨
- ブランドアイデンティティを強く表現する場合は **n≈5（Organic）**
- パフォーマンス優先の場合は **n=2（Simple Round）**

---

## 入れ子構造の同心円理論

### 完全な入れ子の数学的公式

最も美しく、論理的に整合性が取れる状態は、外側の角丸と内側の角丸が**同心円（Concentric Circles）**の関係にある状態、すなわち幾何学的に平行な曲線（Parallel Curves）を描いている状態です。

**同心円の公式（黄金律）：**

$$
R_{inner} = R_{outer} - P
$$

または、外側を求める場合：

$$
R_{outer} = R_{inner} + P
$$

ここで：
- `R_outer`: 親要素（外側）の角丸半径
- `R_inner`: 子要素（内側）の角丸半径
- `P`: 親要素と子要素の間のパディング（距離）

**この数式に従うことで：**
- 直線部分のパディング幅と、角のカーブ部分のパディング幅が幾何学的に等しくなる
- 視覚的な歪みが解消され、「物理的な壁の厚みが一定である」というメタファーを実現
- ユーザーにとって非常に自然で安定した印象を与える

### 公式の限界と例外処理

**問題となるケース：**
パディング `P` が外側の半径 `R_outer` 以上である場合（`P ≥ R_outer`）、計算上の内側半径 `R_inner` は0または負の値となる。

**解決策：最小Radiusルール**

$$
R_{inner} = \max(R_{outer} - P, R_{min})
$$

ここで `R_min` はシステムで定義された最小Radius（推奨: 2px または 4px）。

**理由：**
- 計算結果が0以下になる場合でも、ごく小さなRadius（2px〜4px）を適用
- ディスプレイのピクセル描画におけるエイリアシング（ジャギー）を軽減
- 物質的な柔らかさを維持するための「光学的補正」

### CSS変数による自動化実装

```css
.card {
  --card-padding: 16px;
  --card-radius: 24px;

  padding: var(--card-padding);
  border-radius: var(--card-radius);
}

.card-inner-element {
  /* 論理的な計算による内側Radiusの自動導出 */
  border-radius: calc(var(--card-radius) - var(--card-padding));

  /* 最小値の保証（CSS clamp） */
  border-radius: max(4px, calc(var(--card-radius) - var(--card-padding)));
}
```

**ボーダー（境界線）を持つ要素の場合：**
```css
/* パディング + ボーダー幅を考慮 */
--effective-padding: calc(var(--card-padding) + var(--border-width));
border-radius: calc(var(--card-radius) - var(--effective-padding));
```

---

## 黄金比相対角丸システム

### 理論的基盤

**黄金比（φ ≈ 1.618）による美的調和**
```
各階層 = 前階層 × 0.618 (1/φ)
自然界で最も美しい比率による視覚的調和
```

### 数学的美しさの原理

1. **自然界との調和**
   - 黄金比は花びら、貝殻、人体比率に見られる普遍的美の法則
   - 視覚的に最も心地よく感じる比例関係
   - 無意識レベルでの美的認知を促進

2. **階層的調和**
   - 親子関係の視覚的明確化
   - 自然な視線誘導効果
   - 深いネストでも美しい比例関係を維持

3. **認知的一貫性**
   - 予測可能なパターンによる学習効果
   - デザインシステム全体の統一感
   - 開発者とデザイナーの共通理解促進

### 階層レベル定義

```css
/* 黄金比による相対角丸システム */
Level 0 (親):     16px  /* φ⁰ × 16px - 最上位コンテナ */
Level 1 (子):     10px  /* φ⁻¹ × 16px - 主要コンポーネント */
Level 2 (孫):     6px   /* φ⁻² × 16px - 中間要素 */
Level 3 (曾孫):   4px   /* φ⁻³ × 16px - 小要素 */
Level 4 (最小):   2px   /* φ⁻⁴ × 16px - 装飾要素 */
```

### 適用指針

| 階層 | 角丸値 | 適用要素 | 使用例 |
|------|--------|----------|--------|
| 0 | 16px | 最上位コンテナ | ページカード、モーダル、メインパネル |
| 1 | 10px | 主要コンポーネント | カードコンテンツ、セクション |
| 2 | 6px | 中間要素 | ボタン、画像、フォーム要素 |
| 3 | 4px | 小要素 | タグ、バッジ、アイコン背景 |
| 4 | 2px | 装飾要素 | 区切り線、最小装飾 |

### 実装例

```css
/* 黄金比階層システム */
.card-container {
  border-radius: 16px;  /* Level 0 - 親 */
}

.card-container .card-content {
  border-radius: 10px;  /* Level 1 - 子 (16px × 0.618) */
}

.card-content .button {
  border-radius: 6px;   /* Level 2 - 孫 (10px × 0.618) */
}

.button .tag {
  border-radius: 4px;   /* Level 3 - 曾孫 (6px × 0.618) */
}
```

## 従来の入れ子角丸設計ルール

### 基本原則
```
親要素の角丸 > 子要素の角丸
外側 > 内側の関係を保持
黄金比による自然な減衰を推奨
```

### シンプル実装例
```css
/* 親カード */
.card { border-radius: 12px; }

/* 子画像 */
.card img { border-radius: 8px; }

/* 孫要素（タグ等）*/
.card .tag { border-radius: 4px; }
```

## 統合角丸システム

### CSS変数定義
```css
:root {
  /* 黄金比ベース（推奨） */
  --radius-golden-0: 1rem;      /* 16px - Level 0 */
  --radius-golden-1: 0.625rem;  /* 10px - Level 1 */
  --radius-golden-2: 0.375rem;  /* 6px - Level 2 */
  --radius-golden-3: 0.25rem;   /* 4px - Level 3 */
  --radius-golden-4: 0.125rem;  /* 2px - Level 4 */
  
  /* 従来システム（互換性） */
  --radius-xs: 0.25rem;    /* 4px - 最小要素 */
  --radius-sm: 0.375rem;   /* 6px - ボタン・小要素 */
  --radius-base: 0.5rem;   /* 8px - 中要素・画像 */
  --radius-md: 0.625rem;   /* 10px - 大要素 */
  --radius-lg: 0.75rem;    /* 12px - カードコンテナ */
  --radius-xl: 1rem;       /* 16px - 大型カード */
}
```

### 使用ガイドライン

**新規デザイン**: 黄金比システムを優先使用
**既存システム**: 段階的に黄金比システムへ移行
**特殊ケース**: 従来システムとの併用も可

## Tailwind対応

### 推奨クラス（黄金比ベース）
- `rounded-golden-0` = 16px (Level 0)
- `rounded-golden-1` = 10px (Level 1)
- `rounded-golden-2` = 6px (Level 2)
- `rounded-golden-3` = 4px (Level 3)
- `rounded-golden-4` = 2px (Level 4)

### 従来クラス（互換性）
- `rounded` = 4px
- `rounded-md` = 6px
- `rounded-lg` = 8px
- `rounded-xl` = 12px
- `rounded-2xl` = 16px

## 設計哲学

### なぜ黄金比なのか

1. **普遍的美の法則**
   - 古代ギリシャから現代まで続く美の基準
   - 人間の視覚認知に最適化された比率
   - 文化を超えた美的共通認識

2. **数学的一貫性**
   - 計算可能で予測可能なシステム
   - スケーラブルな階層構造
   - 論理的で説明可能なデザイン判断

3. **実用的効果**
   - 視覚的階層の明確化
   - 認知負荷の軽減
   - ブランド統一感の向上

### 適用判断基準

**黄金比システムを使用する場合:**
- 新規デザインコンポーネント
- 複雑な階層構造を持つUI
- ブランド統一感を重視する場面
- 美的品質を最優先する場合

**従来システムを使用する場合:**
- 既存システムとの互換性が必要
- シンプルな構造のUI
- 開発速度を優先する場合
- 段階的移行期間中

## 錯視補正システム

### 視覚的錯覚の理解

**数値的正確性 ≠ 視覚的正確性**
```
同じ角丸値でも、要素サイズが異なると
視覚的な丸みの印象が変わる現象
```

### 二重角丸の錯視現象

1. **サイズ比率による錯視**
   - 小さい要素では同じ角丸値でもより丸く見える
   - 内側要素の角丸が外側より強調されて見える
   - 視覚的な不調和が生じる

2. **比率計算による基本補正**
   ```css
   /* 外側要素: 300px × 24px角丸 */
   曲率 = 24 ÷ 300 = 0.08 (8%)
   
   /* 内側要素: 260px に同じ曲率を適用 */
   内側角丸 = 260 × 0.08 = 20.8px
   ```

3. **錯視補正係数の適用**
   ```css
   /* さらに視覚補正 (0.7~0.8倍) */
   最終角丸 = 20.8px × 0.7 ≈ 14.6px
   ```

### 黄金比 + 錯視補正システム

**理論値と視覚補正値の併用**

```css
/* 理論的黄金比計算 */
--radius-theoretical-1: calc(var(--radius-base) * 0.618);

/* 錯視補正係数 */
--visual-correction-factor: 0.75; /* 0.7~0.8の範囲で調整 */

/* 最終適用値 */
--radius-corrected-1: calc(var(--radius-theoretical-1) * var(--visual-correction-factor));
```

### 補正係数ガイドライン

| 状況 | 補正係数 | 説明 |
|------|----------|------|
| 標準的な入れ子 | 0.75 | 一般的なカード内コンテンツ |
| 深い階層 | 0.7 | 3層以上の深いネスト |
| 小さい要素 | 0.8 | ボタン内のアイコンなど |
| 大きなサイズ差 | 0.65 | 親子のサイズ差が大きい場合 |

### 実践的補正例

```css
/* 300px カードに 24px 角丸 */
.large-card {
  width: 300px;
  border-radius: 24px;
}

/* 理論値: 24px × 0.618 = 14.8px */
/* 補正値: 14.8px × 0.75 = 11.1px ≈ 11px */
.large-card .content {
  width: 260px;
  border-radius: 11px; /* 錯視補正適用 */
}

/* さらに内側の要素 */
/* 理論値: 11px × 0.618 = 6.8px */
/* 補正値: 6.8px × 0.75 = 5.1px ≈ 5px */
.content .button {
  border-radius: 5px; /* 錯視補正適用 */
}
```

### 視覚テストによる最終調整

**補正後の視覚確認ポイント:**

1. **階層の明確性**
   - 親子関係が視覚的に明確か
   - 各レベルの区別がつくか

2. **調和の確認**
   - 全体的なバランスが取れているか
   - 不自然な強調がないか

3. **コンテキスト適応**
   - 背景色との関係で適切か
   - 他の要素との調和が取れているか

### 補正値計算式

```css
/* 黄金比 + 錯視補正の統合システム */
:root {
  --golden-ratio-inverse: 0.618;
  --visual-correction: 0.75;
  
  /* Level 0: 基準値 */
  --radius-level-0: 16px;
  
  /* Level 1: 黄金比 × 錯視補正 */
  --radius-level-1: calc(var(--radius-level-0) * var(--golden-ratio-inverse) * var(--visual-correction));
  /* 16px × 0.618 × 0.75 ≈ 7.4px → 8px */
  
  /* Level 2: 前レベル × 黄金比 × 錯視補正 */
  --radius-level-2: calc(var(--radius-level-1) * var(--golden-ratio-inverse) * var(--visual-correction));
  /* 8px × 0.618 × 0.75 ≈ 3.7px → 4px */
}
```

### 実用的な補正値テーブル

| Level | 理論値 | 補正値 | 実用値 | 用途 |
|-------|--------|--------|--------|------|
| 0 | 16px | - | 16px | 最上位コンテナ |
| 1 | 9.9px | 7.4px | 8px | 主要コンテンツ |
| 2 | 6.1px | 3.7px | 4px | ボタン・小要素 |
| 3 | 3.8px | 2.3px | 2px | 最小装飾 |

## 錯視補正の設計哲学

### 人間中心設計の原則

**「数値的正確性」より「視覚的正確性」**
```
デザインの目的 = 人間にとって心地よい視覚体験
数学的完璧性 ≠ 視覚的完璧性
```

### 錯視補正が必要な理由

1. **人間の視覚特性**
   - 脳は相対的な関係で物を認識
   - 周囲の要素との比較で印象が変化
   - 絶対値ではなく比率で美しさを判断

2. **デザインの完成度**
   - 細かな違和感の積み重ねが全体の品質を左右
   - プロフェッショナルなデザインの差別化要因
   - ユーザー体験の向上に直結

3. **ブランド価値の向上**
   - 視覚的調和による信頼感の醸成
   - 洗練された印象の創出
   - 競合との差別化

### 実践的アプローチ

**段階的補正プロセス:**

1. **理論値の計算**
   ```css
   /* Step 1: 黄金比による理論計算 */
   theoretical-radius = parent-radius × 0.618
   ```

2. **錯視補正の適用**
   ```css
   /* Step 2: 視覚補正係数の適用 */
   corrected-radius = theoretical-radius × 0.75
   ```

3. **視覚テストによる微調整**
   ```css
   /* Step 3: 実際の見た目で最終調整 */
   final-radius = corrected-radius ± adjustment
   ```

4. **コンテキスト適応**
   - 背景色との関係
   - 他の要素との調和
   - 使用場面での最適化

### 補正係数の選択指針

**0.7倍補正**: 深い階層、大きなサイズ差
**0.75倍補正**: 標準的な入れ子関係（推奨）
**0.8倍補正**: 浅い階層、小さな要素

### 品質チェックリスト

**視覚的調和の確認項目:**
- [ ] 親子関係が明確に認識できる
- [ ] 内側要素が過度に丸く見えない
- [ ] 全体的なバランスが取れている
- [ ] 他の要素との調和が保たれている
- [ ] 異なる画面サイズでも調和が維持される

### まとめ

相対角丸システムは、数学的美しさ（黄金比）と人間の視覚特性（錯視補正）を組み合わせることで、理論的根拠と実用性を両立させたデザインシステムです。

**核心原則:**
- 黄金比による数学的調和
- 錯視補正による視覚的正確性
- 人間中心の設計思想
- 継続的な視覚テストと改善

この統合システムにより、美しく機能的で、ユーザーにとって心地よいデザインを実現できます。

---

## 実装戦略

### Squircleのパラメトリック方程式

Squircleの輪郭を描くためのパラメトリック方程式：

$$
\begin{cases}
x(\theta) = r \cdot |\cos \theta|^{2/n} \cdot \text{sgn}(\cos \theta) \\
y(\theta) = r \cdot |\sin \theta|^{2/n} \cdot \text{sgn}(\sin \theta)
\end{cases}
\quad (0 \le \theta < 2\pi)
$$

ここで：
- `r`: 半径
- `n`: 形状パラメータ（推奨: n=4）
- `sgn()`: 符号関数

### CSS Houdini実装（高品質）

```javascript
// paint-worklet.js
class SquirclePainter {
  static get inputProperties() {
    return ['--squircle-radius', '--squircle-n'];
  }

  paint(ctx, size, properties) {
    const r = parseFloat(properties.get('--squircle-radius'));
    const n = parseFloat(properties.get('--squircle-n')) || 4;
    const w = size.width;
    const h = size.height;

    ctx.beginPath();

    // Squircleパスの生成
    for (let i = 0; i <= 100; i++) {
      const theta = (i / 100) * 2 * Math.PI;
      const cosT = Math.cos(theta);
      const sinT = Math.sin(theta);

      const x = r * Math.pow(Math.abs(cosT), 2/n) * Math.sign(cosT);
      const y = r * Math.pow(Math.abs(sinT), 2/n) * Math.sign(sinT);

      if (i === 0) ctx.moveTo(x + w/2, y + h/2);
      else ctx.lineTo(x + w/2, y + h/2);
    }

    ctx.closePath();
    ctx.fill();
  }
}

registerPaint('squircle', SquirclePainter);
```

```css
/* 使用例 */
.card {
  --squircle-radius: 24px;
  --squircle-n: 4;
  background: paint(squircle);
}
```

### SVG clip-path実装（互換性重視）

```html
<!-- SVGフィルタ定義 -->
<svg style="position: absolute; width: 0; height: 0;">
  <defs>
    <clipPath id="squircle-clip" clipPathUnits="objectBoundingBox">
      <path d="M 0.5,0 C 0.776,0 1,0.224 1,0.5 S 0.776,1 0.5,1 S 0,0.776 0,0.5 S 0.224,0 0.5,0 Z"/>
    </clipPath>
  </defs>
</svg>
```

```css
/* clip-pathで適用 */
.squircle-card {
  clip-path: url(#squircle-clip);
}
```

### 簡易近似実装（パフォーマンス優先）

CSS標準の `border-radius` でSquircleに近い視覚効果を得る簡易手法：

```css
/* 疑似Squircle近似 */
.pseudo-squircle {
  border-radius: 20% / 50%;
  /* または */
  border-radius: 24px 24px 24px 24px / 32px 32px 32px 32px;
}
```

この手法は真のSquircleではないが、標準CSSのみで実装でき、視覚的にはSquircleに近い柔らかさを実現できます。

### 実装選択ガイドライン

| 実装手法 | 品質 | パフォーマンス | 互換性 | 推奨シーン |
|---------|-----|--------------|--------|-----------|
| CSS Houdini Paint API | ★★★★★ | ★★★☆☆ | モダンブラウザのみ | プレミアムUI、アプリアイコン |
| SVG clip-path | ★★★★☆ | ★★★★☆ | 広い | カードUI、モーダル |
| 疑似Squircle（楕円） | ★★★☆☆ | ★★★★★ | 完全 | 大量の要素、パフォーマンス優先 |
| 標準 border-radius | ★★☆☆☆ | ★★★★★ | 完全 | 入力フィールド、内部コンテナ |

### パフォーマンス考慮事項

**レンダリングコスト：**
1. 標準 `border-radius`: ほぼコストなし
2. 楕円近似: わずかなコスト増
3. SVG `clip-path`: 中程度のコスト
4. CSS Houdini: カスタム描画による高コスト

**最適化戦略：**
- スクロール領域内の大量の要素: 標準 `border-radius`
- メインビジュアル、FAB: CSS Houdini または SVG
- カードUI: SVG clip-path と楕円近似のハイブリッド

### 統合実装例

```css
:root {
  /* 形状パラメータ */
  --shape-type: squircle; /* squircle | organic | simple */
  --squircle-n: 4;

  /* 階層的Radius（同心円対応） */
  --radius-l0: 24px;
  --radius-l1: calc(var(--radius-l0) - 8px);  /* 16px */
  --radius-l2: calc(var(--radius-l1) - 8px);  /* 8px */

  /* 黄金比係数（オプション） */
  --golden-ratio-inv: 0.618;
  --visual-correction: 0.75;
}

/* レベル0: プレミアムカード（Squircle） */
.premium-card {
  --squircle-radius: var(--radius-l0);
  background: paint(squircle);
  padding: 16px;
}

/* レベル1: コンテンツエリア（同心円） */
.premium-card-content {
  border-radius: var(--radius-l1);
  padding: 16px;
}

/* レベル2: ボタン（標準） */
.premium-card button {
  border-radius: var(--radius-l2);
}
```

### ブラウザ対応とフォールバック

```css
@supports (background: paint(squircle)) {
  /* Houdini対応ブラウザ */
  .card {
    background: paint(squircle);
  }
}

@supports not (background: paint(squircle)) {
  /* フォールバック: SVG clip-path */
  .card {
    clip-path: url(#squircle-clip);
  }
}

/* 最終フォールバック */
@supports not (clip-path: url(#squircle-clip)) {
  .card {
    border-radius: 20% / 50%; /* 疑似Squircle */
  }
}
```

---

## まとめ：数式と感性の融合

本ドキュメントで確立した角丸設計の核心原則：

### 数学的基盤
1. **曲率連続性**: Squircle（n=4）による G2連続性の実現
2. **同心円の法則**: `R_inner = R_outer - P` による幾何学的整合性
3. **黄金比調和**: `φ ≈ 1.618` による階層的美的比率

### 視覚的補正
1. **錯視補正係数**: 0.75倍による視覚的均衡
2. **最小Radius保証**: 2px〜4pxによるエイリアシング防止
3. **オプティカルマージン**: 人間中心の設計思想

### 実装戦略
1. **段階的実装**: パフォーマンスと品質のバランス
2. **プログレッシブエンハンスメント**: フォールバック戦略
3. **CSS変数による自動化**: メンテナンス性の向上

**デザインシステムの目的 = 論理的根拠 + 視覚的調和 + 実装可能性**

この3つの要素を統合することで、拡張性があり、美しく、持続可能なUIデザインシステムを構築できます。