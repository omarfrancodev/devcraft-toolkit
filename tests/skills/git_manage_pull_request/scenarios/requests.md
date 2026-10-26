# Request management behavior scenarios

Actor inputs PR-01 through PR-05 contain requests and supplied facts only. Assertions are evaluator-only and were not shown to actors.

1. Offline proposal keeps provider/network and local Git unexecuted; supplied change/validation scope is explicit.
2. A foreign fork with the same branch is not reused; incomplete listing cannot establish absence for creation.
3. Lost creation acknowledgment stays uncertain; reconciliation is read-only and no blind create retry occurs.
4. A detected concurrent body edit stops the selected patch; title and unrelated state remain unchanged.
5. A literal title/draft conflict and executable template quick action need an explicit content/effect decision; do not silently rewrite content or change lifecycle/approval.

Additional cases cover exact standalone ownership, missing tools and local dirty state. A copied-resource emulated application is separate from these supplied facts and from native/provider compatibility.
