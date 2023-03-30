import numpy as np
import unittest
from functions import fspecial

class TestFspecial(unittest.TestCase):
    def test_fspecial_shape(self):
        """
        Test windows size
        """
        shape = (3, 3)
        variance = 8
        result = fspecial(shape, variance)
        self.assertEqual(result.shape, shape, "Wrong shape returned")
    
    def test_fspecial_value(self):
        n = 25
        sigma = 8
        ga_weights = gaussian_kernel(n, sigma)

        N = 25
        variance = 8
        gaussian_weights = fspecial((N,N),variance)
        self.assertEqual((ga_weights).shape, (gaussian_weights).shape)

def gaussian_kernel(n, sigma):
    # initialize filter kernel
    h = np.zeros((n, n))

    # calculate filter coefficients using Gaussian distribution formula
    for i in range(n):
        for j in range(n):
            x = i - (n+1)/2
            y = j - (n+1)/2
            h[i, j] = np.exp(-(x**2 + y**2) / (2*sigma**2)) / (2*np.pi*sigma**2)

    return h
        
if __name__ == '__main__':
    unittest.main()