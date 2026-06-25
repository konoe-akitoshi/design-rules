# ガイドライン — 使えるデザインガイドライン

このリポジトリの **思想・既存理論・配色方を「使える形」に統合した、一般UI/UXのデザインガイドライン**。
Apple HIG と同じ温度感（思想と実装の中間）で、設計者が UI を作る/直す/検証するときに直接従う層。

> このガイドラインは**特定のUIに限定されない**（ブランドサイト・読み物・印刷物・道具のすべてに効く）。
> **これ単体でデザインは完結する**（値も `tokens.json` と `values/color-system.md`・`values/spacing-system.md` 等を内包）。AIへの対応は別レイヤー（`../prohibited.md` 等）。

---

## 適用範囲 — A: 一般原則 / B: システム・道具レンズ

集めた思想の大半は**あらゆるUI/UXに効く一般原則**だが、一部は「動的な状態・操作・制御があるとき」だけ効く。混同すると、ブランドページに道具の理屈を当てて外す。だから2層に分ける。

### A. 一般原則（あらゆるUI/UXに**常に**適用）
ブランドサイト・記事・印刷物・道具——ジャンルを問わず効く。
- Rams 抑制 / Bauhaus 用途から形 / Swiss 階層 / Vignelli 秩序 / Norman 認知
- Legibility 可読性 / Tufte data-ink / Alexander パターン / Pragmatism 実用 / Human-Centered 人間中心 / Stewardship 長命
- **題材から構造を導く・汎用テンプレ骨格は禁止・全要素が情報を運ぶ**（→ [01 foundations](./01-foundations.md)）

### B. システム・道具レンズ（観測する状態・操作・制御が**あるときだけ**追加）
ダッシュボード・管理画面・監視・AI Agent・運用ツールなど、動的なシステムを扱うとき上乗せする。
- Cybernetics 観測→判断→制御→フィードバック / 例外状態（空・エラー・読込・権限）/ Raskin 操作コスト / Linear 反復速度

> **Systems Thinking は「最上位概念」ではなく、B のレンズ**。題材が複雑なシステムのときに被せる視点であって、全デザインの前提ではない。
>
> - ブランドページ・記事 → **A だけ**で駆動（Swiss / Vignelli / Rams / Bauhaus が構造と造形を導く）
> - ダッシュボード・道具 → **A + B**

---

## 書き方の核 — 3層

各項目は、思想を投げっぱなしにせず、**その思想を使うための理論**を挟んで使える規則まで降ろす。

```
思想（なぜ）
  ↓ その思想を使うための理論（なぜ効くか・どう運用するか）
使える規則（具体的に何をするか／何を禁じるか）
```

- **思想** … 各思想（Rams / Bauhaus / Swiss / Vignelli / Norman / Tufte …）を1〜2文に圧縮して提示。
- **使うための理論** … その思想が効く仕組み（認知・知覚・システム上の理由）と、運用するための手続き。
- **使える規則** … 生成・修正・検証でそのまま使える命令。値は `../tokens.json` / [color-system](./values/color-system.md)。

---

## 章構成

「層」列が **A=一般（常に）/ A·B=混在 / B=道具レンズ（条件付き）**。ブランドページは A 行だけ、道具は全行を読む。

| 章 | 層 | 関心 | 束ねる思想 |
|----|----|------|-----------|
| [01 foundations](./01-foundations.md) | **A·B** | 設計姿勢・題材から構造・決定順 | Experience Before Expression / Pragmatism / Stewardship / Human-Centered ／（B）Systems Thinking |
| [02 information-structure](./02-information-structure.md) | **A** | 分類・階層・可読性・密度 | Wurman / Legibility / Vignelli / Tufte / Alexander |
| [03 interaction-feedback](./03-interaction-feedback.md) | **A·B** | 操作・認知・フィードバック・注意 | Norman / Calm / Apple HIG ／（B）Cybernetics / Raskin |
| [04 layout-space](./04-layout-space.md) | **A** | グリッド・余白・近接・錯視補正 | Swiss / Ecological Psychology / spacing / optical |
| [05 color](./05-color.md) | **A** | 配色の使い方 | Rams / Calm / Tufte / WCAG / 配色方 |
| [06 typography](./06-typography.md) | **A** | 階層・読み順 | Swiss / Vignelli |
| [07 restraint-form](./07-restraint-form.md) | **A** | 抑制・造形・誠実さ | Rams / Bauhaus ／（B寄り）Linear |
| [08 states-resilience](./08-states-resilience.md) | **B** | 例外状態・耐性 | Stewardship ／（B）Cybernetics / 状態列挙 |
| [09 motion](./09-motion.md) | **A** | アニメーションの是非 | Linear / Apple HIG / Calm |
| [10 accessibility](./10-accessibility.md) | **A** | コントラスト・ターゲット・焦点 | WCAG / Apple HIG |

**実装値（全章が参照）**: [color-system](./values/color-system.md) ・ [spacing-system](./values/spacing-system.md) ・ [border-radius](./values/border-radius.md) ・ [responsive-mobile](./values/responsive-mobile.md)。値の正は [`../tokens.json`](../tokens.json)。

---

## コンポーネント（実用層）

原則（01–10章）を実際の部品へ落とした層。**全60コンポーネント**を [The Component Gallery](https://component.gallery/components/) の体系に沿ってカタログ化し、各部品に本ガイドラインの規則・トークン・状態・a11y を適用した。原則が「なぜ・どう」なら、ここは「この部品は具体的にこう作る」。

- 入口・カタログ・共通規則: **[components/README.md](./components/README.md)**
- 詳細: [forms](./components/forms.md) ・ [actions](./components/actions.md) ・ [overlays](./components/overlays.md) ・ [feedback](./components/feedback.md) ・ [navigation](./components/navigation.md) ・ [display](./components/display.md)

部品を組んで画面にするときは上の[決定順](#決定順ジャンル非依存)（特に「題材から構造を導く」）に従う。部品が正しくても骨格が定番テンプレなら「どこかで見た」画面になる。

---

## 決定順（ジャンル非依存）

見た目から始めない。この順で確定（詳細は [01 foundations](./01-foundations.md)）。`※B` はシステム/道具のときだけ。矛盾は下記「優先順位」で解く。

```
1 目的       … 誰が・何のために・このページ/画面の唯一の仕事は何か
              ※B: 道具なら「何を観測・判断・制御・保守するか」も
2 構造       … 題材から導く（汎用テンプレ骨格を使わない）／分類軸・階層・現在地
3 操作とFB   … 操作対象があるとき。 ※B: システムなら観測→判断→制御→FB を閉じる
4 レイアウト  … グリッド・余白・近接・読み順
5 造形       … 色・タイポ・角丸をトークンから
6 抑制と耐性  … 削れる装飾を削る／a11y／motion　※B: 道具なら例外状態（空・エラー・読込）
7 検証       … チェックリスト・優先順位で矛盾解決
```

---

## 優先順位（矛盾の解決）

ルールが衝突したら **floor（下限）** が勝つ。floor は全章を横断して最優先。

- **可読性の下限**（M-LEGIBILITY）… 「きれい」より「読める」（現在地・関係・階層・状態が判別できる）。
- **判断材料の下限**（M-JUDGMENT-MATERIAL）… ミニマル化・抑制を理由に、判断に必要な情報（現在値・基準値・差分・状態）を削らない。
- **実用性／最終調停**（M-PRAGMATISM）… 原則を教条適用しない。この場面で理解・作業速度・保守性を実際に改善する方を採る。
- ※B（道具のとき）**回復可能性**（M-RECOVERABILITY）… 破壊操作は確認モーダルより undo を優先。
- ※B（道具のとき）**重大変化の可視性**（M-CRITICAL-VISIBILITY）… 静けさを理由に重大なエラー・期限を埋もれさせない。

floor で決まらなければ **レイヤー順（Systems → IA → Interaction → Visual）**で上位を優先（下位＝見た目の都合で上位＝構造を曲げない）。
