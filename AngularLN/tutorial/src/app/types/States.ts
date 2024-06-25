import { Task } from './Tasks';
import { ListFetchingError } from './FetchingError';
// idle / init
type IdleState = {
  state: 'idle';
};
// lodaing list
type LoadingState = {
  state: 'loading';
};
// success fetch
type SuccessState = {
  state: 'success';
  result: Task[];
};
// error on fetching
type ErrorState = {
  state: 'error';
  error : ListFetchingError;
};

export type ComponentListState =
  | IdleState
  | LoadingState
  | SuccessState
  | ErrorState;
