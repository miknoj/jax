# Copyright 2022 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import abc
from typing import Any, List, Optional, Sequence, Tuple, Union
import numpy as np

from jax._src.sharding import Sharding
from jax._src.array import ArrayImpl, Shard
from jax._src.typing import ArrayLike


class Array(abc.ABC):
  dtype: np.dtype
  ndim: int
  size: int
  itemsize: int
  aval: Any

  @property
  def shape(self) -> Tuple[int, ...]: ...

  @property
  def sharding(self) -> Sharding: ...

  @property
  def addressable_shards(self) -> Sequence[Shard]: ...

  @property
  def addressable_data(self, index: int) -> ArrayImpl: ...

  def __init__(self, shape, dtype=None, buffer=None, offset=0, strides=None,
               order=None):
    raise TypeError("jax.numpy.ndarray() should not be instantiated explicitly."
                    " Use jax.numpy.array, or jax.numpy.zeros instead.")

  def __getitem__(self, key, indices_are_sorted=False,
                  unique_indices=False) -> Array: ...
  def __setitem__(self, key, value) -> None: ...
  def __len__(self) -> int: ...
  def __iter__(self) -> Any: ...
  def __reversed__(self) -> Any: ...
  def __round__(self, ndigits=None) -> Array: ...

  # Comparisons

  # these return bool for object, so ignore override errors.
  def __lt__(self, other) -> Array: ...  # type: ignore[override]
  def __le__(self, other) -> Array: ...  # type: ignore[override]
  def __eq__(self, other) -> Array: ...  # type: ignore[override]
  def __ne__(self, other) -> Array: ...  # type: ignore[override]
  def __gt__(self, other) -> Array: ...  # type: ignore[override]
  def __ge__(self, other) -> Array: ...  # type: ignore[override]

  # Unary arithmetic

  def __neg__(self) -> Array: ...
  def __pos__(self) -> Array: ...
  def __abs__(self) -> Array: ...
  def __invert__(self) -> Array: ...

  # Binary arithmetic

  def __add__(self, other) -> Array: ...
  def __sub__(self, other) -> Array: ...
  def __mul__(self, other) -> Array: ...
  def __matmul__(self, other) -> Array: ...
  def __truediv__(self, other) -> Array: ...
  def __floordiv__(self, other) -> Array: ...
  def __mod__(self, other) -> Array: ...
  def __divmod__(self, other) -> Array: ...
  def __pow__(self, other) -> Array: ...
  def __lshift__(self, other) -> Array: ...
  def __rshift__(self, other) -> Array: ...
  def __and__(self, other) -> Array: ...
  def __xor__(self, other) -> Array: ...
  def __or__(self, other) -> Array: ...

  def __radd__(self, other) -> Array: ...
  def __rsub__(self, other) -> Array: ...
  def __rmul__(self, other) -> Array: ...
  def __rmatmul__(self, other) -> Array: ...
  def __rtruediv__(self, other) -> Array: ...
  def __rfloordiv__(self, other) -> Array: ...
  def __rmod__(self, other) -> Array: ...
  def __rdivmod__(self, other) -> Array: ...
  def __rpow__(self, other) -> Array: ...
  def __rlshift__(self, other) -> Array: ...
  def __rrshift__(self, other) -> Array: ...
  def __rand__(self, other) -> Array: ...
  def __rxor__(self, other) -> Array: ...
  def __ror__(self, other) -> Array: ...

  def __bool__(self) -> bool: ...
  def __complex__(self) -> complex: ...
  def __int__(self) -> int: ...
  def __float__(self) -> float: ...
  def __index__(self) -> int: ...

  # np.ndarray methods:
  def all(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, out=None,
          keepdims=None) -> Array: ...
  def any(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, out=None,
          keepdims=None) -> Array: ...
  def argmax(self, axis: Optional[int] = None, out=None, keepdims=None) -> Array: ...
  def argmin(self, axis: Optional[int] = None, out=None, keepdims=None) -> Array: ...
  def argpartition(self, kth, axis=-1, kind='introselect', order=None) -> Array: ...
  def argsort(self, axis: Optional[int] = -1, kind='quicksort', order=None) -> Array: ...
  def astype(self, dtype) -> Array: ...
  def broadcast(self, sizes: Sequence[int]) -> Array: ...
  def broadcast_in_dim(self, shape: Sequence[Union[int, Any]],
                       broadcast_dimensions: Sequence[int]) -> Array: ...
  def choose(self, choices, out=None, mode='raise') -> Array: ...
  def clip(self, min=None, max=None, out=None) -> Array: ...
  def compress(self, condition, axis: Optional[int] = None, out=None) -> Array: ...
  def conj(self) -> Array: ...
  def conjugate(self) -> Array: ...
  def copy(self) -> Array: ...
  def cumprod(self, axis: Optional[Union[int, Tuple[int, ...]]] = None,
              dtype=None, out=None) -> Array: ...
  def cumsum(self, axis: Optional[Union[int, Tuple[int, ...]]] = None,
             dtype=None, out=None) -> Array: ...
  def diagonal(self, offset=0, axis1: int = 0, axis2: int = 1) -> Array: ...
  def dot(self, b, *, precision=None) -> Array: ...
  def flatten(self) -> Array: ...
  @property
  def imag(self) -> Array: ...
  def item(self, *args) -> Any: ...
  def max(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, out=None,
          keepdims=None, initial=None, where=None) -> Array: ...
  def mean(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, dtype=None,
           out=None, keepdims=False, *, where=None,) -> Array: ...
  def min(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, out=None,
          keepdims=None, initial=None, where=None) -> Array: ...
  @property
  def nbytes(self) -> int: ...
  def nonzero(self, *, size=None, fill_value=None) -> Array: ...
  def prod(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, dtype=None,
           out=None, keepdims=None, initial=None, where=None) -> Array: ...
  def ptp(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, out=None,
          keepdims=False,) -> Array: ...
  def ravel(self, order='C') -> Array: ...
  @property
  def real(self) -> Array: ...
  def repeat(self, repeats, axis: Optional[int] = None, *,
             total_repeat_length=None) -> Array: ...
  def reshape(self, *args, order='C') -> Array: ...
  def round(self, decimals=0, out=None) -> Array: ...
  def searchsorted(self, v, side='left', sorter=None) -> Array: ...
  def sort(self, axis: Optional[int] = -1, kind='quicksort', order=None) -> Array: ...
  def split(self, indices_or_sections: ArrayLike, axis: int = 0) -> List[Array]: ...
  def squeeze(self, axis: Optional[Union[int, Tuple[int, ...]]] = None) -> Array: ...
  def std(self, axis: Optional[Union[int, Tuple[int, ...]]] = None,
          dtype=None, out=None, ddof=0, keepdims=False, *, where=None) -> Array: ...
  def sum(self, axis: Optional[Union[int, Tuple[int, ...]]] = None, dtype=None,
          out=None, keepdims=None, initial=None, where=None) -> Array: ...
  def swapaxes(self, axis1: int, axis2: int) -> Array: ...
  def take(self, indices, axis: Optional[int] = None, out=None,
           mode=None) -> Array: ...
  def tobytes(self, order='C') -> bytes: ...
  def tolist(self) -> List[Any]: ...
  def trace(self, offset=0, axis1: int = 0, axis2: int = 1, dtype=None,
            out=None) -> Array: ...
  def transpose(self, *args) -> Array: ...
  @property
  def T(self) -> Array: ...
  def var(self, axis: Optional[Union[int, Tuple[int, ...]]] = None,
          dtype=None, out=None, ddof=0, keepdims=False, *, where=None) -> Array: ...
  def view(self, dtype=None, type=None) -> Array: ...

  # Even though we don't always support the NumPy array protocol, e.g., for
  # tracer types, for type checking purposes we must declare support so we
  # implement the NumPy ArrayLike protocol.
  def __array__(self) -> np.ndarray: ...
  def __dlpack__(self) -> Any: ...

  # JAX extensions
  @property
  def at(self) -> Any: ...
  @property
  def weak_type(self) -> bool: ...
