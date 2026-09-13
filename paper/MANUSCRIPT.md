# Therapeutic Economies

## Protective Selection, Endogenous Capabilities, and Institutional Dependence

Ignacio Adrián Lerer  
Independent Researcher, Buenos Aires, Argentina  
ORCID: 0009-0007-6378-9749  
13 September 2026

## Abstract

This paper develops a theoretical-computational account of institutions that preserve organizations while weakening the capabilities by which those organizations could eventually operate without protection. It joins three literatures that are usually kept apart: the critique of therapeutic culture, evolutionary game theory, and extended evolutionary approaches to institutions. The proposed mechanism is **protective selection inversion**. Protection changes local payoffs so that seeking continued insulation can become more adaptive than investing in productive capability, even while aggregate capability deteriorates. A two-strategy replicator-mutator model couples the population share of protection-seeking organizations to an endogenous capability stock. Four stylized policy regimes are compared with a fixed-capability baseline: unconditional protection, conditional support, open exposure, and a sequenced transition. Across 200 deterministic seeds with declared stochastic shocks, the reference parameterization produces inversion only under unconditional protection. Conditional support and open exposure instead select productive behavior and build capability. A parameter grid contains both positive and negative inversion regions, showing that the result is mechanism-dependent rather than tautological. The model is an existence proof, not an estimate, forecast, or empirical validation for Argentina or any other jurisdiction. Its contribution is to specify how protective institutions can alter both present incentives and the future population of capabilities on which reform depends. It also yields falsifiable implications and a design distinction between protection that teaches and protection that anesthetizes.

**Keywords:** evolutionary game theory; extended evolutionary theory; soft budget constraints; institutional dependence; capability formation; industrial policy; therapeutic culture; protection; policy conditionality

## 1. Introduction

Institutions can fail visibly. Firms close, students fail examinations, and programs exhaust their budgets. They can also fail more quietly by changing what counts as success. Continued operation substitutes for productive improvement; participation substitutes for learning; the preservation of an incumbent organization substitutes for the creation of capabilities that would allow it to survive under independent comparison. When this happens, protection no longer merely cushions a transition. It reorganizes the environment in which strategies are selected.

This paper asks a narrow question: **can unconditional protection generate a selection process in which protection-seeking becomes locally adaptive while productive capability declines?** The question is motivated by a broader cultural analogy. Philip Rieff's account of therapeutic culture describes a shift from institutions that transmit demanding purposes toward institutions organized around the management of subjective well-being (Rieff 1966). Gregorio Luri's polemical idea of *psicosocialismo* extends a related criticism to schooling and public life (Luri 2021). Neither author offers the economic model developed here. The bridge from their cultural diagnosis to political economy is the author's theoretical extension.

I call the relevant institutional configuration a **therapeutic protection regime**: a regime in which support is legitimized and renewed by the vulnerability it preserves, while independent tests of capability are weakened or deferred. “Therapeutic” is analogical, not clinical. The argument is not directed against therapy, disability support, social insurance, developmental policy, or public intervention as such. Good therapy can increase agency; good protection can create capabilities. The target is a feedback structure in which an intervention acquires an interest in the persistence of the condition that warrants it.

The phrase *therapeutic economy* is not claimed as an unprecedented term. In medical anthropology, Vinh-Kim Nguyen used it for the totality of therapeutic options and patterns of resort through which treatment is accessed (Nguyen 2005). That concept concerns treatment, citizenship, and access to care. The present use concerns political-economic protection and capability formation. The more precise term throughout the model is therefore *therapeutic protection regime*.

The paper makes four contributions. First, it distinguishes protection that teaches from protection that anesthetizes without reducing the issue to state versus market. Second, it specifies **protective selection inversion** as a joint change in strategy frequency, capability, and relative payoff. Third, it couples evolutionary strategy dynamics to an endogenous capability stock, so policy changes the population that later reforms will encounter. Fourth, it publishes a dependency-free simulation, fixed-capability baseline, negative cases, sensitivity grid, tests, and release hashes for replication.

The model does not demonstrate that Argentina is a therapeutic economy. Argentina supplies the motivating puzzle, not an identified causal effect. Empirical application would require sectoral data, credible comparison groups, policy timing, rival explanations, and measures that do not define success through the policy being evaluated. The computational exercise establishes only internal sufficiency: the declared mechanism can generate the claimed pattern under explicit assumptions.

## 2. From Therapeutic Culture to Protective Institutions

### 2.1 Rieff and the displacement of institutional purpose

Rieff's argument is not a conventional complaint about psychotherapy. It is a theory of cultural authority. Cultures transmit prohibitions, obligations, and purposes that orient individuals beyond immediate satisfaction. The rise of psychological man changes the center of evaluation: institutions increasingly answer to the individual's demand for well-being rather than asking the individual to answer to inherited ends (Rieff 1966). This is not identical to either markets or government. Consumer culture can multiply satisfactions without purpose, while administration can manage welfare without emancipation.

That symmetry matters. A market may shelter private rents, and a state may impose demanding performance conditions. The relevant distinction is functional. Does the intervention form a capability and expose its results to information the beneficiary cannot control? Or does it replace that test with an internal narrative that treats preservation as proof of value?

Luri applies a related criticism to education. A school can care for students in order to teach them, or it can redefine care as the avoidance of frustration and thereby displace learning as its governing end (Luri 2021). The analogy with economic protection is not identity. Students, firms, workers, and patients are not interchangeable. The common structure is narrower: an institution created to overcome a vulnerability may gain legitimacy from administrating it indefinitely.

### 2.2 Soft budget constraints and the missing cultural mechanism

Kornai's soft budget constraint provides the immediate economic antecedent. An organization behaves differently when it expects losses to be absorbed by another institution. Recurrent subsidies, privileged credit, tax relief, rescue, or barriers to entry weaken the connection between decisions and consequences (Kornai 1986). The concept explains why an expectation of support changes behavior even before a rescue occurs.

The therapeutic-protection hypothesis adds two elements. First, support affects the production of future capabilities, not only present financial discipline. Second, the supported organization's continued existence can become a moral and administrative indicator that validates the support itself. The policy then protects not only an organization from failure but also the policy system from disconfirming information.

This claim has affinities with organizational ecology. Selection operates over organizational forms under environmental constraints, and environments can favor persistence rather than efficiency (Hannan and Freeman 1977, 1989). It also connects to increasing returns and path dependence, where early institutional choices generate self-reinforcing political and organizational investments (Pierson 2000). The distinctive claim here is the coupling of a strategy-selection process with the degradation or formation of a capability stock.

### 2.3 Industrial policy as the strongest rival

The strongest objection is historical: development has often involved protection, credit allocation, state coordination, and public enterprise. The World Bank's study of East Asian growth documented substantial intervention alongside export discipline and performance monitoring (World Bank 1993). Rodrik argues that industrial policy can facilitate discovery when governments and firms learn about productive opportunities, provided institutions can discontinue failures rather than convert experiments into entitlements (Rodrik 2004).

This objection rules out a simple equation between protection and institutional pathology. Exposure can be too abrupt, markets can be distorted, and infant activities can require time to learn. The contrast must therefore be between two architectures:

1. **Formative protection** buys time for learning, specifies review conditions, uses partly independent performance information, and makes future support responsive to results.
2. **Therapeutic protection** treats continued vulnerability as a reason for renewal, permits beneficiaries to influence the test, and weakens the link between support and capability acquisition.

Conditionality is not automatically formative. Poorly chosen targets can induce gaming; sanctions can destroy capacity; export success can reflect rents or favorable prices. Conversely, unconditional support can be justified during a short emergency. The hypothesis concerns repeated feedback over time, not the moral character of one instrument.

## 3. Evolutionary Architecture

### 3.1 Why evolutionary game theory

Evolutionary game theory (EGT) is useful when organizations need not solve a global optimization problem. Strategies spread because they perform relatively well in a local environment. Institutions change those payoffs. A protection-seeking strategy may be socially costly and nevertheless individually adaptive when obtaining continued shelter yields higher organizational fitness than investing in capabilities whose return depends on uncertain exposure.

Let a population contain two stylized strategies:

- **C**, capability-building: investment in productive competence, learning, and external performance;
- **P**, protection-seeking: investment in preserving or enlarging institutional shelter.

The variable \(x_t\in[0,1]\) is the share using P at time \(t\). This is an analytical compression. Real organizations mix strategies, switch incompletely, and contain internal coalitions. The two-strategy form is chosen to make the feedback inspectable.

The policy environment supplies protection \(p_t\), exposure \(e_t\), and conditional review \(q_t\), each bounded between zero and one. Productive capability is a stock \(c_t\in[0,1]\). Payoffs are:

\[
\pi_C = b_C + \alpha c_t + \beta e_t + \gamma p_t e_t q_t - \delta e_t + \varepsilon_t,
\]

\[
\pi_P = b_P + \rho p_t - \eta e_t - \theta q_t p_t - \varepsilon_t.
\]

Capability and exposure reward C; protection rewards P; review makes protected status less attractive; conditional learning allows protection, exposure, and review to interact constructively. The same payoff shock enters with opposite signs to preserve a transparent relative disturbance.

Payoffs are mapped to positive fitness through \(f_i=\exp(s\pi_i)\), where \(s\) is selection strength. The protection-seeking share follows a discrete replicator step with symmetric mutation \(\mu\):

\[
\tilde{x}_{t+1}=\frac{x_t f_P}{x_t f_P+(1-x_t)f_C},
\]

\[
x_{t+1}=(1-\mu)\tilde{x}_{t+1}+\mu(1-\tilde{x}_{t+1}).
\]

Mutation represents experimentation, entry, mistakes, and organizational variation. It prevents purely absorbing boundaries and is not a biological claim about firms.

### 3.2 Endogenous capability

The key extension is that capability evolves:

\[
c_{t+1}=\operatorname{clip}\{c_t
+\phi(1-x_t)(\ell_0+\ell_e e_t)
+\kappa p_t e_t q_t(1-x_t)
-d c_t
-\lambda p_t x_t c_t
+\nu_t\}.
\]

The first gain term represents learning by capability-building organizations. External exposure raises the opportunity and pressure to learn. The second gain term represents formative support, which is strongest when protection is combined with exposure and review. Capability depreciates at rate \(d\). The dependence term \(\lambda p_t x_t c_t\) represents crowd-out, organizational forgetting, rent-seeking specialization, or erosion of routines associated with productive exposure. The capability shock \(\nu_t\) is small and mean-zero.

This equation is a conjectural mechanism, not a measurement model. Each component would require empirical operationalization. The clipping function also means trajectories can saturate at zero or one. Such boundary results should be read as qualitative trap or accumulation regimes under the reference parameterization, not realistic forecasts of complete incapacity or perfect capability.

### 3.3 Extended evolutionary theory mapping

Extended evolutionary approaches emphasize that inheritance and selection are not exhausted by genes. Organisms and groups modify environments; socially learned representations, rules, routines, and constructed niches can persist and alter later selection pressures (Odling-Smee, Laland, and Feldman 2003; Henrich 2004). Applied cautiously to institutions, this suggests an EPT mapping with four elements:

- **Representation:** preserving an incumbent organization is treated as productive success.
- **Vehicles:** statutes, subsidies, administrative routines, accounting categories, professional narratives, and coalition practices.
- **Constructed environment:** entry barriers, rescue expectations, review procedures, and information channels.
- **Differential retention:** organizations and political coalitions skilled at obtaining protection survive and reproduce their routines.

This is a conditional mapping, not proof that an institutional meme or extended phenotype exists. A real application must establish variation, transmission, causal reach, and differential retention. The simulation instantiates a possible feedback architecture only.

### 3.4 Protective selection inversion

A simulated run exhibits protective selection inversion when all three declared conditions hold over the full horizon:

1. \(x_T-x_0\geq0.10\);
2. \(c_T-c_0\leq-0.05\);
3. the mean of \(\pi_P-\pi_C\) after initialization is positive.

The conjunctive definition prevents two errors. A decline in capability alone may result from an adverse shock unrelated to selection. A rise in protection-seeking alone may be harmless if capability continues to grow. Inversion requires that the institutional environment reward P while the capability stock deteriorates.

The term is proposed as a model construct. An exact-phrase search conducted for this release found no prior scholarly use, but that limited audit cannot establish universal lexical priority. The paper therefore makes no absolute coinage claim.

## 4. Simulation Design

### 4.1 Scenarios and baseline

The model compares four stylized schedules over 120 steps:

| Regime | Protection | Exposure | Review | Interpretation |
|---|---:|---:|---:|---|
| Unconditional protection | 0.88 | 0.12 | 0.08 | durable shelter with weak outside information |
| Conditional support | 0.58 | 0.78 | 0.82 | support tied to exposure and review |
| Open exposure | 0.10 | 0.92 | 0.55 | little shelter and high external comparison |
| Sequenced transition | declining | rising | rising | shelter followed by capability-oriented exposure |

For each regime, the endogenous model is paired with a fixed-capability baseline. Both versions share initial states, schedules, seeds, payoff shocks, selection rule, and output equation. They differ only in whether \(c_t\) evolves. The baseline isolates the feedback contributed by endogenous capability rather than serving as a realistic counterfactual economy.

The initial protection-seeking share is 0.30 and initial capability is 0.62. Two hundred seeds are run for every scenario-model pair. Seeds drive declared Gaussian payoff and capability shocks. Because Python's standard pseudorandom generator and every parameter are committed in the repository, the experiment is exactly reproducible in the tested environment without external data or packages.

The activity proxy is

\[
y_t=c_t(1-x_t)+\omega p_t x_t.
\]

It distinguishes capability-supported activity from protected activity. It is not GDP, welfare, employment, or productivity. No policy conclusion should be based on its absolute value.

### 4.2 Reproducibility and integrity controls

The public repository contains source code, tests, generated CSV and JSON data, a dependency-free SVG figure, a machine-readable citation file, and SHA-256 hashes. Continuous integration reruns unit tests, regenerates the experiment, and compares artifacts with the committed checksum manifest. The release excludes copyrighted books, extracted EPUB text, private research notes, credentials, and unpublished operational methods.

The test suite checks state bounds, deterministic replication, baseline capability, policy schedules, the inversion diagnostic, and positive and negative cases. During development, the first diagnostic inspected only a late window. That produced a false negative because capability collapse changed relative payoffs near the boundary after the selection process had already generated the trap. The released diagnostic evaluates the declared full horizon, and a regression test preserves that correction.

## 5. Results

### 5.1 Reference parameterization

Under unconditional protection with endogenous capability, the mean final protection-seeking share is 0.989 and mean final capability is 0.007. All 200 runs satisfy the inversion diagnostic. In the fixed-capability baseline, the share also rises, to 0.954, but capability remains at 0.620 by construction and inversion is therefore absent. This comparison shows why a strategy-only model misses part of the proposed mechanism: protection can change not only which strategy is frequent but also the stock on which subsequent productive adaptation depends.

Conditional support produces the opposite pattern. The mean final protection-seeking share is 0.0076 and capability reaches the upper model boundary. Open exposure yields a similar result, as does the final phase of the sequenced transition. These boundary values are deliberately reported rather than cosmetically rescaled. They reveal that the reference equations generate strong attractors over a long stylized horizon.

| Scenario | Model | Final P share | Final capability | Cumulative activity proxy | Inversion frequency |
|---|---|---:|---:|---:|---:|
| Unconditional protection | Endogenous | 0.9894 | 0.0075 | 51.50 | 1.00 |
| Unconditional protection | Fixed | 0.9536 | 0.6200 | 53.87 | 0.00 |
| Conditional support | Endogenous | 0.0076 | 1.0000 | 116.30 | 0.00 |
| Conditional support | Fixed | 0.0088 | 0.6200 | 74.50 | 0.00 |
| Open exposure | Endogenous | 0.0072 | 1.0000 | 115.51 | 0.00 |
| Sequenced transition | Endogenous | 0.0072 | 1.0000 | 80.04 | 0.00 |

The activity proxy does not establish that open exposure maximizes social welfare. It excludes adjustment costs, distribution, unemployment, market power, strategic capacity, and many other policy-relevant variables. The result is narrower: within the specified mechanism, regimes that make capability valuable and protection contestable select differently from unconditional protection.

### 5.2 Sensitivity and negative cases

A 4 by 4 grid varies the return to protection \(\rho\) over 0.55, 0.75, 0.95, and 1.15 and dependence damage \(\lambda\) over 0, 0.02, 0.048, and 0.08. The grid contains both inversion and non-inversion regions. When the return to protection is 0.55, inversion frequency is zero across every tested dependence value. Higher protection returns create inversion over much of the grid, especially when dependence damage is positive.

The negative region matters epistemically. If the equations guaranteed inversion merely because the scenario was named “unconditional protection,” the simulation would be circular. Instead, high protection is insufficient when it does not create a durable relative payoff advantage. Likewise, dependence damage influences the capability condition but cannot by itself make protection-seeking spread.

The sensitivity exercise is modest. It is not a global robustness analysis, Bayesian calibration, or structural estimation. Further work should vary horizons, initial conditions, functional forms, mutation, shock processes, heterogeneous firms, political feedback, and adjustment costs. The committed grid provides falsifiable negative cases, not comprehensive robustness.

## 6. Rival Explanations and Falsification

### 6.1 Rival mechanisms

At least five rival explanations could generate persistent low capability without a therapeutic protection regime.

**Macroeconomic instability.** Inflation, exchange-rate volatility, sovereign risk, and recurrent crisis can shorten planning horizons and destroy investment even for firms receiving no special protection. If these variables explain capability outcomes while protection expectations add no predictive value, the proposed mechanism is weakened.

**Infrastructure and finance constraints.** Poor logistics, energy, credit, or taxation can make productive organizations appear dependent. Removing protection without correcting complementary failures may select liquidity and scale rather than capability.

**Strategic externalities and learning.** Support may preserve activities whose spillovers, national-security value, or option value are not captured by current market tests. A temporary period of weak measured productivity can be consistent with genuine capability formation.

**Private market power.** Closed or concentrated private markets can reproduce protection-seeking without a large welfare state. The theory concerns insulation from contestable information, not state ownership alone.

**Distributional insurance.** Society may rationally accept efficiency costs to reduce displacement, regional decline, or catastrophic risk. Persistence is not evidence of deception when trade-offs are explicit and democratically authorized.

These rivals are not footnotes. They define what evidence would be necessary before applying the concept to a country or sector.

### 6.2 Observable implications

The theory yields six provisional implications:

1. Support with weak independent review should be followed by greater organizational investment in maintaining eligibility or barriers relative to capability-building investment.
2. Renewal should correlate more strongly with visible incumbent losses than with measured capability gains.
3. The same nominal support should have different long-run effects when paired with export, entry, quality, or productivity tests outside the beneficiary's control.
4. Long-protected sectors should face higher transition costs because capability has become endogenous to the protective environment.
5. Announced withdrawal without credible capability-building complements should generate real harm, not merely reveal pre-existing inefficiency.
6. A sequenced regime should outperform abrupt withdrawal when early support is tied to later exposure and review, but only if the transition commitment is credible.

The thesis would be falsified or substantially narrowed if high, weakly conditional protection did not predict protection-seeking behavior after credible controls; if capability routinely rose under such regimes without independent exposure; if conditional review produced no difference; or if observed persistence were better explained by measurable spillovers and explicit social insurance choices.

### 6.3 An empirical design for Argentina

Argentina is a plausible case for inquiry because of its recurrent trade barriers, sectoral privileges, macroeconomic instability, and uneven export performance. Plausibility is not identification. A serious design should construct a sector-year panel recording tariff and non-tariff protection, subsidy expectations, effective entry, policy renewal, export exposure, productivity, innovation, worker capabilities, and political organization.

Possible designs include staggered policy changes, synthetic controls for sectors exposed to different reforms, matched firms near eligibility thresholds, and event studies around credible changes in rescue expectations. Qualitative process tracing would be needed to test whether organizations reallocated effort toward protection-seeking and whether policymakers redefined survival as success. Outcome measures should be external to the supporting program.

The causal graph should include macroeconomic volatility, exchange-rate regimes, infrastructure, taxation, credit constraints, global commodity shocks, sector technology, firm age and size, market power, and political connections. Without these controls, the therapeutic label risks becoming an ideological synonym for any intervention the observer dislikes.

## 7. Normative and Policy Implications

The model does not recommend indiscriminate liberalization. If protection has already weakened capability, immediate withdrawal can be destructive precisely because the institutional history changed the population. A student who was not taught does not learn when the examination becomes harsher; a firm deprived of complementary infrastructure does not acquire it when a tariff disappears.

The appropriate design question is whether support contains an emancipation pathway. Four tests follow:

- Does the intervention build a capability that can persist with less of the same intervention?
- Is performance measured with information the beneficiary cannot fully manufacture?
- Are review dates, comparison classes, and consequences specified ex ante?
- Does failure change future allocation while preserving humane transition support for persons?

The last distinction is essential. Firms and policies can be discontinued; persons retain moral status and claims to assistance. A capability-oriented regime can be demanding toward organizations while financing worker insurance, retraining, mobility, and local adjustment. Conflating the preservation of a particular producer with the protection of its workers converts organizational incumbency into social justice.

The therapeutic metaphor also has a moral hazard of its own. It can stigmatize disability, illness, poverty, or legitimate dependence. For that reason, this paper rejects comparisons with sheltered workshops or occupational therapy. Clinical therapy and disability support address concrete human needs. The analogy is restricted to institutional feedback in which care rhetoric blocks evaluation and makes dependence self-validating.

## 8. Discussion

The central result is an existence claim. When protection directly rewards protection-seeking, exposure and review are weak, and capability is damaged by dependence, a locally rational strategy can spread while the stock required for later autonomy declines. The institution selects bearers adapted to itself.

This result links EGT and EPT. EGT explains relative strategy change under altered payoffs. EPT draws attention to the environment that institutions construct and transmit. Endogenous capability joins them: the constructed environment affects not only current success but the traits, routines, and resources available in the next period. Policy is therefore both an allocator and a producer of future agents.

The framework also clarifies why reform coalitions are difficult. Beneficiaries, workers, administrators, and politicians may all prefer present continuity to uncertain future gains. No actor needs to believe the regime is optimal. Concentrated transition losses and dispersed counterfactual benefits are enough. As capability declines, the factual case for continued protection can even become stronger in the short run. The regime partly produces the vulnerability cited in its defense.

But the model should not be mistaken for confirmation. Its binary strategies, representative capability stock, exogenous policy schedules, fixed population, symmetric mutation, and bounded state variables omit heterogeneity, entry and exit, fiscal constraints, political bargaining, innovation networks, trade retaliation, demand, and welfare distribution. The reference run reaches boundaries, a sign of strong stylization. The results are transparent enough to criticize because all equations and artifacts are public.

## 9. Conclusion

The opposition between care and cruelty is too crude for institutional design. Protection may be necessary, just, and productive. The question is what it selects and what it builds. A regime protects formatively when it uses support to create capabilities that can later withstand more independent information. It becomes therapeutic in the specific critical sense developed here when preserving vulnerability becomes both its operating result and its evidence of success.

Protective selection inversion supplies a testable mechanism for that possibility. In the published simulation, unconditional protection can make protection-seeking adaptive while capability collapses; conditional support, exposure, and review can reverse the direction of selection. These are model outcomes, not facts about a country. The next step is empirical: determine when real protective institutions buy learning, when they buy political peace, and when they quietly select a population increasingly fitted to protection itself.

## Data and Code Availability

All synthetic code, tests, parameters, generated data, figures, and release hashes are available in the public repository associated with this paper. The simulation requires Python 3.10 or newer and no third-party packages. The repository contains no copyrighted source books or private research material.

## Competing Interests

The author declares no competing interests.

## AI Assistance Disclosure

Generative AI assisted with drafting, code implementation, consistency checks, and document production under the author's direction. The author selected the research question and conceptual thesis, reviewed the argument, and retains responsibility for all claims, errors, and interpretations. All simulation logic and outputs are openly inspectable.

## References

Hannan, Michael T., and John Freeman. 1977. “The Population Ecology of Organizations.” *American Journal of Sociology* 82 (5): 929–964. https://doi.org/10.1086/226424.

Hannan, Michael T., and John Freeman. 1989. *Organizational Ecology*. Cambridge, MA: Harvard University Press.

Henrich, Joseph. 2004. “Cultural Group Selection, Coevolutionary Processes and Large-Scale Cooperation.” *Journal of Economic Behavior & Organization* 53 (1): 3–35. https://doi.org/10.1016/S0167-2681(03)00094-5.

Kornai, János. 1986. “The Soft Budget Constraint.” *Kyklos* 39 (1): 3–30. https://doi.org/10.1111/j.1467-6435.1986.tb01252.x.

Luri, Gregorio. 2021. *La mermelada sentimental: Cinco años de artículos en The Objective*. Madrid: Ediciones Encuentro.

Nguyen, Vinh-Kim. 2005. “Antiretroviral Globalism, Biopolitics, and Therapeutic Citizenship.” In *Global Assemblages: Technology, Politics, and Ethics as Anthropological Problems*, edited by Aihwa Ong and Stephen J. Collier, 124–144. Malden, MA: Blackwell.

Odling-Smee, F. John, Kevin N. Laland, and Marcus W. Feldman. 2003. *Niche Construction: The Neglected Process in Evolution*. Princeton, NJ: Princeton University Press.

Pierson, Paul. 2000. “Increasing Returns, Path Dependence, and the Study of Politics.” *American Political Science Review* 94 (2): 251–267. https://doi.org/10.2307/2586011.

Rieff, Philip. 1966. *The Triumph of the Therapeutic: Uses of Faith after Freud*. New York: Harper & Row.

Rodrik, Dani. 2004. “Industrial Policy for the Twenty-First Century.” UNIDO working paper. https://drodrik.scholar.harvard.edu/publications/industrial-policy-twenty-first-century.

World Bank. 1993. *The East Asian Miracle: Economic Growth and Public Policy*. New York: Oxford University Press for the World Bank.
