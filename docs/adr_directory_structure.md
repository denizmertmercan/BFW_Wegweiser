# Architectural Decision Record: Repository Directory Structure

## Status

Proposed

## Context

The repository combines an offline Python data pipeline with a static web visualizer. Three structural conventions were evaluated to organize these components symmetrically.

## Evaluated Options

### Priority 1: src/ and web/

- Characteristics: Conventional layout matching standard Python packaging and static web roots.
- Strengths: Broad tooling support; likely recognized automatically by linters, test runners, and hosting platforms.
- Trade-offs: Names reflect generic directory conventions rather than specific pipeline roles.

### Priority 2: builder/ and viewer/

- Characteristics: Functional pairing reflecting the offline compiler and static visualizer model.
- Strengths: Accurately represents system data flow directly in folder names.
- Trade-offs: Non-standard layout that may require explicit configuration in tooling and test environments.

### Priority 3: python/ and web/

- Characteristics: Platform-oriented pairing designating respective runtimes.
- Strengths: Clear separation of technology stacks across contributors.
- Trade-offs: Focuses on implementation language rather than architectural responsibilities.

## Tentative Decision

The project appears to favor Priority 1 (src/ and web/) for tooling compatibility and standard deployment workflows, while retaining Priorities 2 and 3 as documented alternatives.
