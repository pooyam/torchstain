from .numpy_macenko_normalizer import NumpyMacenkoNormalizer
from .torch_macenko_normalizer import TorchMacenkoNormalizer

def MacenkoNormalizer(backend='torch'):
    if backend == 'numpy':
        return NumpyMacenkoNormalizer()
    elif backend == "torch":
        return TorchMacenkoNormalizer()
    else:
        raise Exception(f'Unknown backend {backend}')
