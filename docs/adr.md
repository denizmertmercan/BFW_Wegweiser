# Architectural decisions

## 1. Static precomputed routing data over a live API

**Status:** Accepted

**Context:** Deployment targets are a standalone kiosk now, possibly phones
later, with no confirmed hosting budget. The routing algorithm and
destination scope (whole building) are still in flux. The team isn't
confident designing a live Python↔JS runtime protocol.

**Decision:** Python is an offline build tool: it preprocesses the
zone/portal graph and exports everything the frontend needs — routing
lookup tables, coordinates, names, tag groupings — as one static JSON file.
The JS frontend only performs lookups against this file at runtime. No live
server or API.

Rejected alternative: reimplementing the graph/algorithm directly in JS
(as done in `Wegweiser_Frontend/frontend/script.js`). That duplication has
already caused drift — its `findPath` has the same directed-graph bug we
fixed on the Python side, because the two copies were never kept in sync.

**Consequences:**

- Zero hosting cost/infra now; the same static files work for a local kiosk
  and, later, phones (hosted, or served locally over the building's Wi-Fi).
- Graph changes mean rerunning the build step and redistributing one file —
  no schema versioning, no migration.
- If live editing or instant cross-device propagation is ever needed, a thin
  HTTP endpoint can wrap the same Python preprocessing code later — nothing
  built now is wasted.

## 2. Usage/feedback analytics deferred and decoupled from routing

**Status:** Accepted

**Context:** Usage data (popular destinations, where users get stuck) is
wanted to improve the algorithm/instructions. Analytics is a write path
(client → collector), fundamentally different from the read-only static
routing data, so it can't reuse the JSON file mechanism.

**Decision:** Not built now. When added, treat it as an independent
component: start with local logging during the kiosk-only phase (zero
infra), move to a third-party privacy-focused analytics service or a
minimal event-collection endpoint once phones are supported. Never store
data traceable back to individual users; define a privacy/consent policy
before collecting anything.

**Consequences:**

- No premature infra/backend built.
- Whichever option is chosen later, it doesn't affect the routing
  architecture.
- Privacy policy decided deliberately upfront, not retrofitted.
