# 正解ブループリント — primeui.com

題材＝**サイトを速く作る開発ツール**（"Build sites fast. Fear no code."）。
sitemap → wireframe → コード → 完成サイト、という**ビルド・パイプライン**が題材の native な様式。
meta description: "Prime UI is the missing foundation for AI-generated websites. Go from sitemaps and wireframes to production-ready Next.js and Tailwind CSS code in minutes."

## トークン（実測）
- 地: **近黒** `#040406` / パネル `#121316` / 境界 `#2F3037` / muted `#9194A1`（= gray-50/60）。純黒は避けている。
- ライト面も併用（テンプレ showcase は白地・`#0b0c0e`/`#2a2b33` のインク）。dark/light 両モードが売り。
- アクセント: グレー〜銀のグラデ見出し（`#8d91a0`→`#838695`）＋ **緑のステータス**（perfの巨大数字 `#BAEBD5→#124D32`、チェック `#20AC4F`）＋ 一部で青/藍（`#2563EB`/`#1F3290`）。実質「near-black ＋ 1アクセント ＋ 緑ステータス」。
- 書体: **font-sans = グロテスク系セミボールド**（tracking タイト、見出しは `tracking-tighter`〜`-0.2rem`）／ **font-mono** がラベル・番号・統計・"Search..."・コードに多用（mono が identity の核）。

## セクション構成（順）
0. **Nav** — Home / Blog / Pricing / Documentation ＋ CTA。
1. **Hero** — h1 "Build sites fast.<span>Fear no code.</span>"（"Fear no code." はグレー銀グラデ）＋ サブ "…on ideas that build" ＋ "Join 1k+ clients today" ＋ CTA（**Explore templates**［塗り］/ **Start for free**［線］）＋ mono の "Search..." 入力モック（sitemap 起点）。
2. **Trusted by Creators & Businesses** — ロゴウォール（Forbes / Modal / Dagster / Digsouth / Statsig / Deno / Case Status）。
3. **01 — Start with a sitemap**（"Outline the vision"）— サイト構造を最初に描く。
4. **02 — Experiment quickly** — ワイヤーフレームで素早く試す。
5. **03 — Export to code.**（"That really works."）— production-ready Next.js + Tailwind を出力。"Built for consistent results. No prompt-engineering."
6. **Complete site.**（"Ready to take off."）— パイプラインの到達点（中央寄せの締め）。
7. **Crafted by humans. Scaled with AI.** — "Exceptional website templates for all projects"（テンプレ showcase グリッド、白地）。
8. **Clean code.**（Core Web Vitals）— 巨大な緑の数字 **0.2s FCP / 0.4s LCP / 0ms TBT**。"Core Web Vitals tested for optimal UX."
9. **Crafted-in details** — **Light and dark modes** / **Polished components**（"subtle animations, micro interactions… Less assembly, more shipping."）/ **Markdown support** / **SEO**（"Never think about SEO again — clean tags, correct links, properly sized images."）。
10. **Pricing — "Need a site? Start with Prime UI."** — **Personal $99**（One-time fee, "For solo builders shipping sites fast."）/ **Business $299**（One-time fee, "For teams scaling projects together."）。緑チェックの機能リスト。"Join 1k+ clients today."
11. **FAQ — "Your questions, answered."** — 5問: What kind of sites can I build with Prime UI? / Does Prime UI generate the full design for my site? / How does licensing work? / Do you work with agencies? / What support do you offer?
12. **Footer** — Home / Blog / Pricing / Documentation / Privacy Policy / Terms & Conditions。

**実セクション数 N ≈ 12〜13**（nav・footer 含む大ブロック）。

## 我々の旧ビルドとの差（#10 旧版）
旧 10-prime-ui.html は **Hero ＋ build パイプライン(signature) ＋ feature strip ＋ footer の約4ブロック**＝ 実物の 1/3。how-it-works の番号ステップ・**テンプレ showcase**・**Core Web Vitals 統計**・**feature details**・**Pricing**・**FAQ** が丸ごと欠落＝**不合格**。全長（上記0–12）で作り直す。
