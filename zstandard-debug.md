Trying to use the `--json-compress` option I introduce fails with a mysterious stack 
trace:

Here the CLI log:
```
INFO:root:2019-06-26T15:28:00.509Z: JOB_MESSAGE_BASIC: Finished operation Read daring-runway-211808:data.reddit_test+Normalise comments+Key by thread id+Group comments by thread ID/Reify+Group comments by thread ID/Write
INFO:root:2019-06-26T15:28:00.588Z: JOB_MESSAGE_BASIC: Executing operation Group comments by thread ID/Close
INFO:root:2019-06-26T15:28:00.646Z: JOB_MESSAGE_BASIC: Finished operation Group comments by thread ID/Close
INFO:root:2019-06-26T15:28:00.712Z: JOB_MESSAGE_BASIC: Executing operation Group comments by thread ID/Read+Group comments by thread ID/GroupByWindow+Get threads+Create JSON examples+add random key+group by key/Reify+group by key/Write
INFO:root:2019-06-26T15:28:10.556Z: JOB_MESSAGE_BASIC: Finished operation Group comments by thread ID/Read+Group comments by thread ID/GroupByWindow+Get threads+Create JSON examples+add random key+group by key/Reify+group by key/Write
INFO:root:2019-06-26T15:28:10.623Z: JOB_MESSAGE_BASIC: Executing operation group by key/Close
INFO:root:2019-06-26T15:28:10.665Z: JOB_MESSAGE_BASIC: Finished operation group by key/Close
INFO:root:2019-06-26T15:28:10.738Z: JOB_MESSAGE_BASIC: Executing operation group by key/Read+group by key/GroupByWindow+get shuffled values+split train and test/ParDo(_TrainTestSplitFn)+serialize test examples+write test/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write test/Write/WriteImpl/WindowInto(WindowIntoFn)+write test/Write/WriteImpl/GroupByKey/Reify+write test/Write/WriteImpl/GroupByKey/Write+serialize train examples+write train/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write train/Write/WriteImpl/WindowInto(WindowIntoFn)+write train/Write/WriteImpl/GroupByKey/Reify+write train/Write/WriteImpl/GroupByKey/Write
INFO:root:2019-06-26T15:32:56.013Z: JOB_MESSAGE_BASIC: Autoscaling: Resizing worker pool from 1 to 2.
INFO:root:2019-06-26T15:33:17.639Z: JOB_MESSAGE_DETAILED: Autoscaling: Raised the number of workers to 2 based on the rate of progress in the currently running step(s).
INFO:root:2019-06-26T15:37:56.044Z: JOB_MESSAGE_BASIC: Autoscaling: Resizing worker pool from 2 to 3.
INFO:root:2019-06-26T15:38:23.598Z: JOB_MESSAGE_BASIC: Autoscaling: Resizing worker pool from 3 to 4.
INFO:root:2019-06-26T15:38:24.231Z: JOB_MESSAGE_DETAILED: Autoscaling: Raised the number of workers to 3 based on the rate of progress in the currently running step(s).
INFO:root:2019-06-26T15:38:24.273Z: JOB_MESSAGE_DETAILED: Resized worker pool to 3, though goal was 4.  This could be a quota issue.
INFO:root:2019-06-26T15:38:45.451Z: JOB_MESSAGE_DETAILED: Autoscaling: Raised the number of workers to 4 based on the rate of progress in the currently running step(s).
INFO:root:2019-06-26T15:42:57.726Z: JOB_MESSAGE_BASIC: Autoscaling: Resizing worker pool from 4 to 5.
INFO:root:2019-06-26T15:43:19.457Z: JOB_MESSAGE_DETAILED: Autoscaling: Raised the number of workers to 5 based on the rate of progress in the currently running step(s).
INFO:root:2019-06-26T15:43:51.340Z: JOB_MESSAGE_BASIC: Finished operation group by key/Read+group by key/GroupByWindow+get shuffled values+split train and test/ParDo(_TrainTestSplitFn)+serialize test examples+write test/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write test/Write/WriteImpl/WindowInto(WindowIntoFn)+write test/Write/WriteImpl/GroupByKey/Reify+write test/Write/WriteImpl/GroupByKey/Write+serialize train examples+write train/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write train/Write/WriteImpl/WindowInto(WindowIntoFn)+write train/Write/WriteImpl/GroupByKey/Reify+write train/Write/WriteImpl/GroupByKey/Write
INFO:root:2019-06-26T15:43:51.418Z: JOB_MESSAGE_DEBUG: Executing failure step failure48
INFO:root:2019-06-26T15:43:51.453Z: JOB_MESSAGE_ERROR: Workflow failed. Causes: S12:group by key/Read+group by key/GroupByWindow+get shuffled values+split train and test/ParDo(_TrainTestSplitFn)+serialize test examples+write test/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write test/Write/WriteImpl/WindowInto(WindowIntoFn)+write test/Write/WriteImpl/GroupByKey/Reify+write test/Write/WriteImpl/GroupByKey/Write+serialize train examples+write train/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write train/Write/WriteImpl/WindowInto(WindowIntoFn)+write train/Write/WriteImpl/GroupByKey/Reify+write train/Write/WriteImpl/GroupByKey/Write failed., The job failed because a work item has failed 4 times. Look in previous log entries for the cause of each one of the 4 failures. For more information, see https://cloud.google.com/dataflow/docs/guides/common-errors. The work item was attempted on these workers:
  beamapp-theomatussiere-06-06260824-sxqr-harness-09vc,
  beamapp-theomatussiere-06-06260824-sxqr-harness-09vc,
  beamapp-theomatussiere-06-06260824-sxqr-harness-dv1s,
  beamapp-theomatussiere-06-06260824-sxqr-harness-ngnm
INFO:root:2019-06-26T15:43:51.597Z: JOB_MESSAGE_DETAILED: Cleaning up.
INFO:root:2019-06-26T15:43:52.255Z: JOB_MESSAGE_DEBUG: Starting worker pool teardown.
INFO:root:2019-06-26T15:43:52.289Z: JOB_MESSAGE_BASIC: Stopping worker pool...
INFO:root:2019-06-26T15:46:24.319Z: JOB_MESSAGE_DETAILED: Autoscaling: Reduced the number of workers to 0 based on the rate of progress in the currently running step(s).
INFO:root:2019-06-26T15:46:24.369Z: JOB_MESSAGE_BASIC: Worker pool stopped.
INFO:root:2019-06-26T15:46:24.403Z: JOB_MESSAGE_DEBUG: Tearing down pending resources...
INFO:root:Job 2019-06-26_08_24_11-3743465527142250923 is in state JOB_STATE_FAILED
Traceback (most recent call last):
  File "reddit/create_data.py", line 394, in <module>
    run()
  File "reddit/create_data.py", line 389, in run
    result.wait_until_finish()
  File "/Users/theomatussiere/Documents/reddit-data/conversational-datasets/venv/lib/python2.7/site-packages/apache_beam/runners/dataflow/dataflow_runner.py", line 1122, in wait_until_finish
    (self.state, getattr(self._runner, 'last_error_msg', None)), self)
apache_beam.runners.dataflow.dataflow_runner.DataflowRuntimeException: Dataflow pipeline failed. State: FAILED, Error:
Workflow failed. Causes: S12:group by key/Read+group by key/GroupByWindow+get shuffled values+split train and test/ParDo(_TrainTestSplitFn)+serialize test examples+write test/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write test/Write/WriteImpl/WindowInto(WindowIntoFn)+write test/Write/WriteImpl/GroupByKey/Reify+write test/Write/WriteImpl/GroupByKey/Write+serialize train examples+write train/Write/WriteImpl/ParDo(_RoundRobinKeyFn)+write train/Write/WriteImpl/WindowInto(WindowIntoFn)+write train/Write/WriteImpl/GroupByKey/Reify+write train/Write/WriteImpl/GroupByKey/Write failed., The job failed because a work item has failed 4 times. Look in previous log entries for the cause of each one of the 4 failures. For more information, see https://cloud.google.com/dataflow/docs/guides/common-errors. The work item was attempted on these workers:
  beamapp-theomatussiere-06-06260824-sxqr-harness-09vc,
  beamapp-theomatussiere-06-06260824-sxqr-harness-09vc,
  beamapp-theomatussiere-06-06260824-sxqr-harness-dv1s,
  beamapp-theomatussiere-06-06260824-sxqr-harness-ngnm
```

Stack driver doesn't log anything, no warning, error, critical... Except for the 
last error that is logged by the CLI.

No clear direction on how to debug :neutral_face:.