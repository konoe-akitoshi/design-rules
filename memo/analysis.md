# 検証 — この集めた情報は「特定UI限定」か「一般UI/UX指針」か

## 問い

「ガイドラインはシステム/道具用」と前段で結論づけたが、本当にそうか。
集めた情報（philosophy / principles / theory）の原典に当たり、各思想を **一般（あらゆるUI/UX）** か **システム・道具特化（動的な状態・操作が前提）** で分類する。

判定の基準: ブランドサイト・読み物・印刷物・静的ページにも効くなら「一般」。観測する状態・操作・制御が無いと成立しないなら「特化」。

---

## 分類（design-philosophy-map.md「設計判断への変換」表より）

| 判断軸 | 思想 | 一般 / 特化 | 根拠 |
|--------|------|------------|------|
| 抑制 | Rams / Calm | **一般** | 「可能な限り少なく」はあらゆる視覚物に効く。Ramsは工業製品・印刷で確立 |
| 工学性 | Bauhaus | **一般** | 「形は用途・素材から導く」は全造形の原理 |
| 階層 | Swiss（International Typographic Style） | **一般** | 起源が**ポスター・ブランド・印刷**。むしろ静的ページが本場 |
| 秩序 | Vignelli / Wurman | **一般** | Vignelliは企業VI・サイン・書籍。一般デザインそのもの |
| 再利用性 | Alexander | **一般** | パターン言語は建築発、全設計に適用 |
| 認知 | Don Norman | **一般** | affordance/feedback は操作対象があれば全UIに（リンク・ボタンでも） |
| 読みやすさ | Legibility | **一般** | 現在地・階層・関係が読めることは全ページの条件 |
| 情報量 | Tufte | **一般寄り** | data-ink（装飾を削る）は普遍。高密度の話だけデータUI寄り |
| 実用性 | Pragmatism | **一般** | 「効果で正当化・教条化しない」は設計態度として普遍 |
| 人間中心 | Human-Centered | **一般** | 人間の認知・誤り・習熟を含めるのは全UX |
| 保守性 | Stewardship | **一般寄り** | 長命性・経年耐性はブランドにも効く。例外状態の話だけ道具寄り |
| 空間性 | Ecological / Physicalization | 一般寄り | 近接・配置=関係はGestaltで普遍。グラフ/地図UIだけ特化 |
| 操作 | Raskin | **特化寄り** | 操作コスト・モードは「反復操作のある道具」前提 |
| 操作感 | Linear / Apple | **特化寄り** | 反復作業SaaS・アプリの体感。静的ページには薄い |
| 制御 | **Cybernetics** | **特化** | 観測→判断→制御→FB は**制御できる動的システムが必須**。静的ページに無い |
| 全体性 | **Systems Thinking / Fuller** | **枠組み（特化に見せている主因）** | これを「最上位概念」に置いたことで全体が道具色に染まる |

---

## 結論

**集めた情報の核は、一般的なUI/UX指針である。** ユーザーの見立てが正しい。

- 16軸のうち **11〜12が一般**（Rams, Bauhaus, Swiss, Vignelli, Wurman, Alexander, Norman, Legibility, Tufte, Pragmatism, Human-Centered, Stewardship）。これらはブランドサイト・読み物・印刷物にもそのまま効く。Swiss/Vignelliに至っては**むしろ静的・印刷が本場**。
- 明確に**道具特化なのは Cybernetics（制御ループ）だけ**。Raskin / Linear / Apple / 空間性は「操作や反復や関係がある時」の条件付き。

### では、なぜ「道具用」に見えたのか（narrowing の3原因）

1. **枠組み**: `design-philosophy-map.md` が **Systems Thinking を最上位概念**に置いた。これで一般原則まで「システムの翻訳」という色眼鏡で読まれる。
2. **例示**: `対象領域 = サーバー / Kubernetes / CMS / LLM / ロボット / 可視化` が全部ツール。例が限定を示唆してしまう。
3. **私の翻訳**: ai-judgment / guidelines が Cybernetics・状態・観測判断制御FB を**核として重く取った**（service-monitorは駆動できたが、ブランドページを駆動できなかった原因）。

つまり「ガイドラインが道具用」なのではなく、**一般原則の上に"システム思考"という枠とツール例を被せ、私がその枠を核として翻訳した**結果、道具特化に見えていた。

---

## 含意（どう直すべきか）

層を分ける:

```
A. 一般原則（あらゆるUI/UXに常に適用）
   Rams 抑制 / Bauhaus 用途から形 / Swiss 階層 / Vignelli 秩序 /
   Norman 認知 / Legibility 可読性 / Tufte data-ink / Alexander パターン /
   Pragmatism 実用 / Human-Centered 人間中心 / Stewardship 長命
   ＋（前段で見つけた）「構造は題材の native な様式から導く・テンプレ骨格禁止・全要素が情報を運ぶ」

B. システム/道具レンズ（動的な状態・操作・制御がある時だけ追加適用）
   Cybernetics 観測→判断→制御→FB / 状態(空・エラー・読込) / Raskin 操作コスト / Linear 反復速度
```

- Systems Thinking は「最上位概念」ではなく **Bのレンズ**に降ろす。
- こうすれば、ブランドページは **A だけで駆動**でき（Swiss/Vignelli/Rams/Bauhaus が構造と造形を導く）、service-monitor は **A+B** で駆動できる。
- 「特定UIに限定されていない」という原典の性格が、構造にも反映される。
