# Coursework evidence

Use these headings to organise your own results and explanations. Replace
bracketed prompts and remove unused prompts. Supplied headings are permitted
reuse; the evidence and explanation must be your own. Refer to short saved
logs rather than pasting entire CI logs.

Staff will not open your private GitHub repository. Save PR pages and CI
runs as PDFs or screenshots, with short log excerpts, in `evidence/` and
give their paths below alongside the URLs.

Complete and commit this file with your other documentation before the final
release checks. Record the final release hash, CI run and fresh-checkout outcome
in the separately submitted `SUBMISSION.txt`, outside the repository, and
submit the final CI run as a separate PDF or screenshot.

## 1. Starting point and Git review

- Starting commit: 588fb96ed012ecb5a1525c9da39634efbce4b0ff
- Reused lab files, tests and examples: My original calculator.py and test_calculator.py are my own work. The coursework supplied files reused are batch_calculator.py, batch_runner.py, the CSV data and expected output examples, the supplied evidence and submission templates.
- Feature branch and PR: calculator-extension[add the pull request URL and saved PDF screenshot in evidence]
- Self-review: I checked that the original calculator was preserved, and the new batch processing implementation was added. I also checked that the initial test and CI workflow were included and the supplied runner and CSV fixtures were present.  I also modified .github/workflows/ci.yml so pushes to calculator-extension also trigger the workflow.

## 2. Test failure, diagnosis and fix

Plan this before fixing the chosen missing requirement or defect. An initially
missing feature is acceptable; retain the test in the final suite.

- Requirement and retained test: R5, test_batch_calculator.py function test_batch_addition
- Expected result and actual failure: The test calls process_calculation("add", "4", "6") and expects ("OK", 10, ""). Instead, the function raised NotImplementedError because its implementation had not yet been completed.
- Before/fix commits: Before commit: ee7bd111c3e69e87caf4ce680396edf1181df30f. Fix commit: 55bbee406ee8421f0297dc28cf8a08a3a60912ea
- Failing/passing local runs: Failing command: python3 -m pytest -v. Output saved in evidence/local-before.txt. Passing run: Passing local run: python3 -m pytest -v Result: 7 passed, 0 failed Output saved in evidence/local-after.txt. Command: python3 -m pytest -v. Result: 28 passed, 0 failed. Evidence: evidence/local-r5.txt
- Failing/passing CI runs: Failing CI run: https://github.com/wall960/Calculator/actions/runs/45159746037/job/137641760977. Matching commit: ee7bd111c3e69e87caf4ce680396edf1181df30f. Saved files: evidence/ci-before.pdf and evidence/ci-before.txt. Passing CI run: https://github.com/wall960/Calculator/actions/runs/45224311498/job/137866588689. Matching commit: 55bbee406ee8421f0297dc28cf8a08a3a60912ea. Saved files: evidence/ci-after.pdf and evidence/ci-after.txt.
- CI diagnosis: The workflow was triggered by a push to the calculator-extension branch. It used an ubuntu-latest runner and executed the tests job. The Run the tests step failed because test_batch_addition() called the unfinished process_calculation() function, which raised NotImplementedError. The six existing calculator tests passed, while the new batch addition test failed. Pytest returned exit code 1, causing the GitHub Actions job to fail.
- Cause and implementation fix: The initial cause was that process_calculation() contained a NotImplementedError placeholder instead of an implementation. I use operation validation by removing surrounding whitespace and checking whether the operation is one of the four supported operations. I also strip whitespace from both operands and convert them into floating point values using float(), and invalid conversions would return INVALID_NUMBER. I use math.isfinite() to reject non finite values, I check the permitted range of -1000 to 1000 was in place for both operands, and that neither operand has more than three decimal places. The second operand is checked if it is zero when the selected operation is division. I then call the corresponding original calculator function add() subtract() multiply() divide(). Finally i return the result in the form ("OK", result, "") for successful calculations. The error priority order is such that unknown operations are checked first, invalid numbers are checked second and division by zero is checked last. The error return format is ("ERROR", "", error_code)



## 3. Repeatable checks and local hook

- Common check script: scripts/check.sh. Local invocation: ./scripts/check.sh. CI invocation: ./scripts/check.sh. Local result: 28 tests passed, exit status 0. CI result: Successful Github Actions run. URL: https://github.com/wall960/Calculator/actions/runs/45234875783/job/137903809509. Saved files: evidence/ci-check_script.pdf, evidence/check-script-permissions.txt, evidence/local-check-script.txt and evidence/ci-check_script.txt.
- Prerequisites and hook installation: python3 -m pip install -r requirements-dev.txt. git config core.hooksPath .githooks. The first command installs the relevant python development dependencies, including pytest. The second tells Git to use the version controlled .githooks directory. .githooks/pre-commit is executable and invokes ./scripts/check.sh.
- Blocked commit attempt: Base commit: ad987cd. Temporary test: test_precommit_demo.py. Test function: test_precommit_blocks_commit. Passings tests: 28. Failing tests: 1. Commit result: Rejected. Saved evidence: evidence/precommit-blocked.txt. Git's HEAD remained at ad987cd after the failed attempt. test_precommit_demo.py remained staged after the failed commit.
- Permitted commit after the fix: Temporary failing test: Removed. Test suite: 28 passed, 0 failed. Commit message: Add version-controlled pre-commit hook. Short commit hash: 6b933bf. Saved evidence: evidence/precommit-allowed.txt. Git executed the hook, the tests passed, and the commit was permitted.
- Hook limitations and independent CI checks: It is a local installation, meaning the hook isnt automatically activated by cloning. Each developer must configure core.hooksPath. Hooks can also be bypassed as Git allows a user to use git -c core.hooksPath=/dev/null commit. Github actions independently runs the test script when the configured push or pull requests occur. Therefore, even if a developer doesnt install or bypasses the local hook, the CI workflow still provides a separate quality gate.

The hook may use the same failure case as section 2 or another case. A blocked
commit attempt has no new commit hash; identify its base commit and changes.

## 4. Native and container batch runs

- Native normal/mixed runs: [commands and saved output/diagnostic paths]
- Container build/run commands and image tag: [README reference or commands]
- Input/output transfer: [how files enter and leave the container]
- Mixed-run interpretation: [summary, one error and later successful records]
- Python version and Docker environment: [what you used]

## 5. Container checks in CI during development

- Checked-out source commit and CI run: [hash, URL and saved file in evidence/]
- Test gate, image build and smoke-test outcomes: [steps and results]
- Smoke fixture and expected-output check: [paths and what is asserted]
- Failure handling: [why failed tests stop the build and wrong output fails CI]

## 6. Reproduction notes

- Checkout tested during development: [commit]
- Documented setup and commands tried: [README reference]
- Outcome and any limitations: [your results]

The final fresh checkout must test the declared release commit. Record its
outcome in `SUBMISSION.txt` after the documentation is committed, CI passes
and the final commit is tagged. Do not create another commit just to insert
that commit's own hash or CI-run URL into this file.
