# Bayesian-Statistics-Activity-5
Activity 5: Coding the sample scripts in Python

An activity worked with groupmates (Angelica Añinon, Jonna Apolinar, Diego Emmanuel Corder, Maria Chrislene Reis, and Mark Anthony Viray)


## Script/Code (1st Picture)

```python
import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.65, 1.8, num = 50)
test = np.linspace(0, 2)
uniform_dist = sts.uniform.pdf(mu) + 1

uniform_dist = uniform_dist/uniform_dist.sum()
beta_dist = sts.beta.pdf(mu, 2, 5, loc = 1.65, scale = 0.2)
beta_dist = beta_dist/beta_dist.sum()
plt.plot (mu, beta_dist, label = 'Beta Dist')
plt.plot (mu, uniform_dist, label = 'Uuniform Dist')
plt.xlabel ("Value of $\mu$ in meters")
plt.ylabel ("Probability density")
plt.legend()
```

## Script/Code (2nd Picture)

```python
import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.65, 1.8, num = 50)
test = np.linspace(0, 2)
uniform_dist = sts.uniform.pdf(mu) + 1

def likelihood_func(datum, mu) :
   likelihood_out = sts.norm.pdf(datum, mu, scale = 0.1)
   return likelihood_out/likelihood_out.sum()

likelihood_out = likelihood_func(1.7, mu)

plt.plot(mu, likelihood_out)
plt.title("Likelihood of $\mu$ given observation 1.7m")
plt.ylabel("Probability Density/Likelihood")
plt.xlabel("Value of $\mu$")
plt.show()
```

## Script/Code (3rd Picture)

```python
import scipy.stats as sts
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.65, 1.8, num = 50)
test = np.linspace(0, 2)
uniform_dist = sts.uniform.pdf(mu) + 1

uniform_dist = uniform_dist/uniform_dist.sum()
beta_dist = sts.beta.pdf(mu, 2, 5, loc = 1.65, scale = 0.2)
beta_dist = beta_dist/beta_dist.sum()
plt.plot (mu, beta_dist, label = 'Beta Dist')
plt.plot (mu, uniform_dist, label = 'Uuniform Dist')
plt.xlabel ("Value of $\mu$ in meters")
plt.ylabel ("Probability density")
plt.legend()

def likelihood_func(datum, mu) :
   likelihood_out = sts.norm.pdf(datum, mu, scale = 0.1)
   return likelihood_out/likelihood_out.sum()

likelihood_out = likelihood_func(1.7, mu)

plt.plot(mu, likelihood_out)
plt.title("Likelihood of $\mu$ given observation 1.7m")
plt.ylabel("Probability Density/Likelihood")
plt.xlabel("Value of $\mu$")
plt.show()

unnormalized_posterior = likelihood_out * uniform_dist
plt.plot(mu, unnormalized_posterior)
plt.xlabel("$\mu$ in meters")
plt.ylabel("Unnormalized Posterior")
plt.show()
```

## Screenshot of the Output

![activity 5 1](https://github.com/mariachrislenereis/Bayesian-Statistics-Activity-3/assets/168893458/96b7d85e-25dd-444d-a8bf-1e64af96cb5d)


![activity 5 2](https://github.com/mariachrislenereis/Bayesian-Statistics-Activity-3/assets/168893458/93b2c20b-d91f-4b59-9562-b0ea0371f9db)


![activity 5 3](https://github.com/mariachrislenereis/Bayesian-Statistics-Activity-3/assets/168893458/c1279f95-dc7c-4e90-bbf7-e0862494a8d0)

## Note

For educational purposes.
