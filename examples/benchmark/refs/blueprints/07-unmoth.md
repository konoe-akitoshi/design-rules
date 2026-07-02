# Blueprint — unmoth.com （正解ページの構造抽出）

題材: ブランディング・スプリント・スタジオ（"From invisible to unforgettable" / 14日でブランド一式）。実測 refs/unmoth.html（Framer SSR・極小エレガント・dark）。
native な様式 = **編集的なインデックス付き作品集 + 14日スプリントの工程票**。テンプレ骨格ではなく「番号付き章立て(001–006)で読ませるエージェンシーの語り」と「14日タイムライン」から構造を立てる。
RESTRAINT が identity だが **1画面ではなく、番号付きの複数セクションを持つフルページ**。余白とヘアラインで沈黙させ、各章に1つだけ signal を灯す。

## ブランド（題材から導く）
- 地: 冷たいニアブラック **#08090A**（real）。面 #121314 / 罫 #262727（rgb 38,39,39, real）。純黒/純白を避ける。
- ink: near-white **#F4F3F0**（見出し ≈18:1）/ 本文 #C7C6C1 / 二次 #8E8E8B(≈5.6:1) / ラベル #7C7C79(≈4.5:1, real の #5C5D5E はUI 3:1 未満なので a11y のため引き上げ)。
- アクセント: **whisper champagne #C9A86C**（1色のみ・焦点ノード/在席ドット/hover/focus にだけ灯す）。real はほぼモノクロ＋緑ドット1点 → "暗闇の一点の光"という invisible→unforgettable の主張に合わせ bespoke の温かい1光に置換。
- 見出し書体: **Faculty Glyphic**（real・グリフィック装飾セリフ／Google Fonts・単一ウェイト400）。
- 本文/UI 書体: **Geist**（real・グロテスク／Google Fonts 300–600）。
- CTA: 透明地＋ヘアライン枠 pill、hover で accent 枠。非対称padding。

## セクション構成（実ページ順 = 構築順）
| # | セクション | label | 内容 |
|---|-----------|-------|------|
| nav | **Nav** | — | unmoth wordmark（orbit mark）/ Work・Services・Process・Pricing・FAQ / "Get sprint" CTA |
| 0 | **Hero** | — | 焦点 orbit グリフ（一点だけ点灯）→ h1 "From invisible to unforgettable." / sub "Your brand in just 14 days." / "Get sprint" CTA / 在席ステータス |
| 1 | **Manifesto** | — | 大セリフ中央寄せ1文: "Let the world see what you've been working on in the dark."（real meta copy） |
| 2 | **Work / Use cases** | 001 | 作品 4件: Spacia / Essential / Dockr / New Form Factor（各 category＋抽象ビジュアル）＋ "View more work" |
| 3 | **Services** | 002 | "We turn ideas into brand systems with everything you need to launch, scale, and stand out." ＋ 9項目リスト（Research and moodboard / Logo variations / Typographic identity / Color system / Visual Assets / Brand guidelines / Iconography / Applications Examples / Imagery & Photo Style） |
| 4 | **Marquee** | — | クライアント/ケース名の静かな横スクロール（reduced-motion で停止） |
| 5 | **Process** | 003 | "A complete process. Just faster." ＋ 3段: Kick Off / Refine / Deliver（各説明文 real） |
| 6 | **Timeline** | 004 | "You don't have 3 months… we only need 2 weeks… a perfect match." ＋ 14日レール（01/03/07/12/14 のマイルストーン, real numbers） |
| 7 | **Pricing** | 005 | 単一オファー "Brand Design" / "The main offer, 14 days." / Timeline:14 Days・Output:Full Brand System・Support:Figma + PDF / "Let's Talk" |
| 8 | **FAQ** | 006 | 5問（details/summary）: changes during process / beyond core identity / ownership / right for startups / how to start（全て real 回答） |
| 9 | **Footer** | — | 最終CTA "Get sprint" ＋ Navigation / Email(contact@unmoth.com) / LinkedIn / Twitter ＋ wordmark ＋ © 2026 Unmoth |

実セクション数 = **10ブロック（nav + hero + 8 content/footer ≈ 0–9）**。旧 07-unmoth.html は hero＋1行manifesto＋極小footer の3ブロックのみ（実物の約3割）＝不合格。

## 反テンプレ判断
- ヒーローは split でなく **中央 near-empty ＋ 単一焦点グリフ**（unmoth 実物の沈黙の型・主役は"一点の光"）。
- 特徴は等分3カラムに逃げず: Work=作品タイル / Services=罫線リスト / Process=3段 / Timeline=日付レール と様式を変える。
- 番号 001–006 は real のインデックス（章の順序を運ぶ）として保持。装飾連番ではなく案内子として使う。
- eyebrow 乱用なし。各章に1つだけ accent を灯す（焦点・在席ドット・hover/focus）。
- a11y: skip-link / landmarks / focus-visible / details accordion / 本文4.5:1・UI3:1 / 48-44px touch / reduced-motion。
