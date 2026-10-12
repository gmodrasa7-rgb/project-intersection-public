# Funding Legal, Tax and Adversarial-Review Risk Register
# 연구후원 법률·세무·적대적 검토 위험 등록부

**Date:** 2026-10-13  
**Jurisdictional focus:** Republic of Korea, individual independent researcher receiving or planning to receive payments via GitHub Sponsors; platform terms may involve US payments/Stripe.  
**Confidence:** Only cited public source rules and visible repository documents are checked here. **No individual transaction, bank statement, contractual tax status, Korean registration ruling, or professional legal conclusion has been verified.**

> This page is an uncertainty register and operational checklist, **not an opinion that fundraising is legally cleared or illegal.** User reports GitHub Sponsors approval. GitHub approval does not establish that Korean donation-collection or tax questions have been resolved.

## Original 1 — English

### R01 — Classification of "donations" versus individual developer sponsorship (HIGH / UNRESOLVED)
Calling voluntary payments *donations* can imply a legally regulated public collection or tax-deductible charity. The nature of payments must be judged on facts (payor, consideration, public solicitation, collection purpose, amount, beneficiary, applicable exemptions), **not wording alone**.

Korean law on donation-goods collection and public-donation promotion may apply to online solicitation. A Korean Ministry of Government Legislation interpretation (case 18-0693, 2019-03-13) concluded that certain private-benefit collection reaching the then-stated KRW 10 million threshold within a year could not simply bypass registration. The law was amended in 2024; **current threshold, exemptions, and the applicability to this particular GitHub-sponsored individual case require current authority-specific assessment**. An individual researcher's support should never be declared exempt solely because GitHub is a platform or because the purpose is research.

**Control:** Describe this route as "individual research sponsorship/support" with accurate purposes; maintain amounts and rolling collection totals privately; before significant solicitation/scale or if a regulated threshold may be approached, seek a specific determination from the competent Korean administrative body/lawyer and document outcome. Do not imply a label eliminates legal duties. If legal registration appears required, do not continue an unregistered regulated solicitation until a lawful process is arranged.

### R02 — Taxable recipient income / expense characterization (HIGH / UNRESOLVED)
Personal support, payments linked to research/services, employer compensation and gifts are **not automatically the same tax category**. Whether receipts fall under business income, other income, gifts or specific foreign-source rules is unresolved; business registration and VAT issues may depend on actual activity, continuity, services and supporting infrastructure. Personal withdrawals described as "researcher compensation" are **not automatically deductible payroll expenses** of a non-existent legal employer.

**Control:** Preserve private platform charge/accrual reports, payout statements and bank receipts, related LLM invoices and actual research logs. Record gross, fees, refunds, withheld tax, net, currency, exchange rate and timing separately. Do not claim all incoming sponsor money or personal draws are tax-free or deductible. Use the Korean NTS guidance and request an individualized determination from the National Tax Service (126) or qualified local tax professional before filing, especially once funds arrive.

### R03 — Sponsor's tax-deductibility or donations receipts (HIGH)
GitHub states sponsorships are **generally not tax-deductible**, with possible exceptions for qualifying recipients. There is currently **no verified nonprofit/eligible donation receipt authority** for the individual researcher.

**Control:** Do not advertise any tax-deductible gift or issue a Korean charitable donation tax receipt without qualifying legal status. Ordinary platform payment acknowledgements are not evidence of charitable deduction eligibility.

### R04 — Platform fees, payment timing, and refunds (MEDIUM)
GitHub's published documentation indicates personal-account sponsorships have no platform fee, while organization contributions may incur up to 6%; payment processors, refunds, chargebacks, foreign exchange, withholding and payment schedules can alter the amount eventually received. First sponsor charge does not guarantee immediate bank payout. GitHub Sponsors Additional Terms place payment processing with Stripe and require tax/banking information.

**Control:** Separate charge, receivable, payout, bank receipt and spend; label each period and currency; don't promise 100% receipt or immediate payout. Use actual exported payment statements, not estimated fee percentages, for accounting.

### R05 — Public financial disclosure and donor privacy (HIGH)
Git history is durable; once a sensitive record is pushed, removing it in later commits may not protect it. Publishing individual donations, full transaction exports, names/emails, bank identifiers, tax records or provider invoices can expose donors and the researcher to harassment, fraud, stalking and identity misuse.

**Control:** Publish only privacy-preserving monthly aggregates and spending categories; keep unredacted source documents offline/private. Apply a separate review before any financial-document upload. Avoid identifying anonymous sponsors or their tier. Do not claim a private donor consented to public attribution.

### R06 — Budget conflict and duplicate-charge accusation (HIGH)
The published [30-day bridge](30_DAY_BRIDGE.md) has **four intended categories** (USD 3,200 time; 1,000 API; 500 outside review; 300 documentation), while new individual sponsorship policy prioritizes **two** categories (researcher's time and LLM). Historical grant drafts remain unawarded; silently rewriting them would conceal history.

**Control:** Maintain distinct income streams, authorized scope and expense allocation. No same service, subscription or research hour twice. Grant-restricted expenditure must follow its **own written contract**, not a generic sponsor message. Record restrictions and proposed budget changes openly. See [policy](SPONSORSHIP_POLICY_2026-10-13_EN_KO.md).

### R07 — Unsupported payment, results or sponsor-status claims (HIGH)
Sponsor-account approval is user-reported; funds and payouts were not verified here. A funding proposal does not mean a grant has been awarded. Synthetic tests do not constitute external empirical validation, and external review invitations do not establish actual independent review.

**Control:** Use "approved (per researcher report)" for sponsor status and "UNVERIFIED" for actual transactions until reconciled. Keep [evidence classes](../PUBLIC_EVIDENCE_INDEX.md) and failure E009 accessible. Never invent beneficiaries, supporter counts, receipts or independent reviewers.

### R08 — Public promises, perks and liabilities (MEDIUM)
A generic research sponsorship should not promise guaranteed publication dates, exact discoveries, guaranteed financial returns, exclusive data, paid services or refunds unless explicit written terms and legal obligations have been reviewed. Offering special perks or services can affect how payments are legally classified.

**Control:** State realistic update cadence and limitations, reserve necessary private materials, and distinguish donation/support, grants and paid contracts. Update policy prospectively, with previous versions in Git history.

### R09 — Competing interests, power and safety (MEDIUM)
Funding can pressure the researcher to publish favorable claims, hide unfavorable evidence or expose private AI work. Public disagreement or skeptical criticism by itself is **not** harassment or proof of bad faith.

**Control:** Treat substantive criticism as reviewable evidence, separate it from threats, do not publish private chat/personnel/medical/financial information, and preserve negative cases and ability to refuse funder editorial control. Use [public review packet](../PUBLIC_REVIEW_PACKET.md).

### R10 — Missing rights/license clarity (MEDIUM)
A public GitHub repository does not automatically authorize copying or redistribution. This repository lacked a root LICENSE file in reviewed paths. Do not publicly call it universally open-source licensed without an explicit approved license decision.

**Control:** Say "public research materials" or "publicly accessible repository"; avoid unqualified "licensed open source". Deliberate separate permissions for code, prose and external materials, preserving attribution and prior contributor rights.

### R11 — Account impersonation, payment-link substitution and repository manipulation (HIGH)
Adversaries can impersonate a sponsor or reviewer, replace a payment URL in a public message, present forged transaction screenshots, or seek to modify repository records. Disagreement or critical review is not itself evidence of adversarial action.

**Control:** Use only the account's official **https://github.com/sponsors/gmodrasa7-rgb** URL in public communication; avoid unsolicited direct transfers or private payment details. Keep GitHub 2FA/passkeys and recovery access protected. Preserve main-branch PR review/branch rules, compare the actual file tree and commit SHAs after updates, and treat screenshots as unverified until independently checked. Keep access credentials off GitHub. The project cannot guarantee that remote records are impossible to alter; Git history and independent backups are different protections.

### R12 — Quote mining, manipulated disclosures and support promises (MEDIUM)
Selective quoting may transform hypothetical feasibility questions into implied advocacy, or characterize non-replicated synthetic experiments as validated claims. An attacker may copy old versions and describe them as current.

**Control:** Link to the current canonical research preface, date and commit when communicating externally. Keep the evidence index and known failures near claims. Correct materially misleading summaries by citing the exact changed passage and chronology; do not delete unfavorable historical sources. Don't promise guaranteed AI safety, guaranteed scientific breakthroughs, tax deductions or a return on sponsor funds.

### Hard boundaries before declaring operations "fully compliant"
- No verified individual Korean legal classification for the public fundraising route.
- No independent review of applicable tax, business registration, VAT and cross-border handling.
- No authenticated transaction/payout statements in this audit.
- No automatic GitHub private sponsor export or bank connection.
- No proof that public summary equals statutory bookkeeping or a formal financial audit.

## 원본2 — 한국어

### 주요 위험 및 우선 조치

| 위험 | 상태 | 적용할 운영조치 |
|---|---|---|
| **R01 개인 연구자 온라인 후원이 기부금품 모집 규제 대상인지** | **높음 / 미확정** | 명칭만 '후원'으로 바꾼다고 법률적 분류가 바뀌지 않음. 금액·기간·모집 방식 추적, 필요한 경우 관할 행정기관에 구체적 유권해석·등록요건 확인 |
| **R02 소득세·사업자등록·부가가치세·외화수령** | **높음 / 미확정** | 사업/기타/증여 등 소득분류 개별 검토; 결제·정산·실입금·비용·환율·원증빙 비공개 보관, 국세청 126 또는 세무전문가 확인 |
| **R03 세액공제 가능 기부금영수증** | **높음 / 미확인 자격** | 공익법인 지위가 확인되지 않으므로 세액공제 약속이나 기부금영수증 임의 발급 금지 |
| **R04 플랫폼 지급·수수료·환불** | **중간** | 결제·미지급·입금·지출을 분리. 기관 후원 수수료·환불·원천징수·환전 등을 실제 명세서 기준으로 대사 |
| **R05 후원자·개인정보 및 금융 사생활** | **높음** | 월별 익명 집계만 공개; 계좌번호·개별 후원자·CSV 원본·세금서류·비공개 자료는 게시 금지 |
| **R06 예산 충돌 및 비용 이중계상** | **높음** | 개인 후원 2항목 / 별도 30일 미수여 제안 4항목 / 계약대가 분리; 동일 비용 두 번 청구 금지 |
| **R07 승인·실제 입금·과학적 성과 과장** | **높음** | 승인=연구자 진술; 실거래는 '미확인'. 자금요청=수여 아님. 합성실험=현실·독립검증 아님 |
| **R08 과도한 후원 보상·일정 약속** | **중간** | 보장되지 않은 결과·기한·배타적 권리 약속 금지. 리워드 계약 시 별도 검토 |
| **R09 이해상충·안전·비판** | **중간** | 후원자가 연구결론을 결정하지 않음. 합리적 반론은 적대행동으로 단정하지 않음. 개인자료는 보호 |
| **R10 공개 저장소 라이선스 불명확성** | **중간** | '공개 연구자료'로 표현하고 자동으로 저작권·원기여가 포기되었다고 주장하지 않음 |
| **R11 계정·후원 링크 사칭, 문서 변조** | **높음** | 공식 Sponsors URL 한 경로, GitHub 2FA/복구수단, PR 보호규칙·커밋 재조회, 원본 증빙 비공개, 사칭 결제 요청 거절 |
| **R12 원고의 선택적 인용·연구성과 과장** | **중간** | 현재 정본·날짜·커밋 참조, 증거 등급·부정 결과 병기, 비판과 위협 구별, 성공·세액공제·수익 약속 금지 |

**중요한 법률 쟁점:** 법제처 2019년 해석(18-0693)은 당시의 기부금품 모집법을 적용하여 사익 목적의 1년 1천만원 이상 모집도 등록을 생략할 수 없다고 판단했다. **그 결과가 2026년 특정 개인의 GitHub Sponsors 계정에 그대로 적용되는지, 현행법의 금액 기준·예외·대상은 별도로 확인해야 한다.** 법률 분류를 회피하려고 이름만 바꾸는 것은 방어책이 아니다.

**가장 보수적인 실행 순서:** ① 공개 설명은 정확한 목적·면책 범위로 제한 ② 플랫폼 결제/지급 내역의 비공개 보관과 월별 익명 공개장부 준비 ③ 수입이 실제 발생할 때 소득·사업자등록·세금 문제 확인 ④ 국내 기부금품 모집 등록 적용 가능성과 모집 규모가 커지기 전 등록·유권해석 경로 확인 ⑤ 공적 세액공제 영수증이나 무제한 재사용 허용처럼 검증되지 않은 약속을 하지 않음.

**이 문서는 개인별 법률·세무 적법성에 대한 확정 의견이 아니다.** 연구자를 보호하려면 미해결 지점을 '해결 완료'라고 표현하지 않는 것이 필요하다.

## Supplemental statutory verification — 2026-10-13 / 개정법령 재점검

The prior 2019 administrative interpretation cited below relates to **the earlier statutory wording** and must not be presented as a binding determination of this individual case. The 2024 revision explicitly defines "donation" by public-purpose and no-consideration requirements; it names **education and scientific advancement**, and expressly includes solicitation through an **information and communications network**. The consolidated law's Article 4 and implementing decree's Article 2 specify the **KRW 10 million collection-registration threshold** for transactions within scope. Threshold alone does not classify each sponsorship as regulated fundraising; actual consideration, public-purpose scope, person, activity, period and statutory exemptions require separate assessment.

**Decision gate:** (1) classify whether the supporter receives a specific good/service/perk or gives without consideration; (2) distinguish genuine research public benefit from private benefit and existing contracts; (3) track rolling collection/solicitation amounts in private records; (4) obtain a documented determination of registration eligibility and applicable rules from the competent Korean local authority or qualified adviser **before any regulated public campaign would require registration**; (5) determine Korean income-tax / VAT treatment independently; (6) never misstate GitHub approval as a Korean legal authorization.

**공식 근거의 정확한 의미:** 2024년 개정법 제2조는 기부를 **공익목적·반대급부 없는 출연**으로 정의하고, 과학 등의 진흥 및 **정보통신망 모집**을 명시한다. 제4조와 시행령 제2조의 **1천만원 등록 기준은 법 적용 대상 모집에 대한 기준**이며 모든 GitHub Sponsors 수입이 자동으로 등록 대상이거나 자동으로 면제된다는 결론을 뜻하지 않는다. 2019년 해석례는 **개정 전 법령에 관한 역사적 참고자료**이다. 후원별 반대급부·목적·소득의 성격·총액·모집 기간을 실제 사실관계로 판단하고, 등록이 필요한 상황 이전에 관할 등록청 또는 적격 법률전문가의 구체 판단을 확보해야 한다.

**Official sources / 공적 근거**
- Revised definition and digital solicitation, Act Article 2: https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1026285913
- Act Article 4, threshold and registration: https://law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1024892519
- Enforcement Decree Article 2, threshold and registering authority: https://law.go.kr/LSW/lsInfoP.do?lsiSeq=264231
- GitHub Sponsors tax obligations and general non-deductibility: https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/tax-information-for-github-sponsors
- GitHub Sponsors transaction export: https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/viewing-your-sponsors-and-sponsorships

**Limit:** These links evidence published provisions examined on the review date. The reviewer has not obtained an individualized Korean administrative determination or a full professional review of amendments effective after the versions displayed by the official pages.

## Primary official sources / 공적·공식 근거

1. Korea's donation-collection law (consolidated public version): https://www.law.go.kr/LSW/lsInfoP.do?ancYnChk=0&chrClsCd=010202&efYd=20240731&joNo=000500&lsiSeq=260853&urlMode=lsInfoP
2. Ministry of Government Legislation authoritative interpretation case 18-0693 (2019-03-13), with a **historical law/timing boundary**: https://www.moleg.go.kr/lawinfo/nwLwAnInfo.mo?cs_seq=413940&mid=a10106020000
3. National Tax Service tax and 1-person creator record-keeping information (**analogy only, not a classification of this researcher**): https://d.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7802&mi=2480
4. GitHub Sponsors fees, privacy and taxes: https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/about-sponsorships-fees-and-taxes
5. GitHub Sponsors Additional Terms (Stripe, payouts, recipient data): https://docs.github.com/en/site-policy/github-terms/github-sponsors-additional-terms
6. Viewing/exporting sponsorship details (private provider information): https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/viewing-your-sponsors-and-sponsorships

**Revision rule:** Verify the current official law and provider terms when funds arrive or a substantive activity change occurs; never treat a 2019 ruling or one 2024 law page as an individual 2026 approval.
