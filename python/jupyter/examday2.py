{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world!\n"
     ]
    }
   ],
   "source": [
    "print(\"hello world!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'D:\\\\CODE\\\\python\\\\jupyter'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = [1, 2, 3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "b?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_numbers(a, b):\n",
    "    \"\"\"\n",
    "    add two numbers together\n",
    "    - - - - -\n",
    "    the sum : type of arguments\n",
    "    \n",
    "    \"\"\"\n",
    "    return a + b\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "add_numbers??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add_numbers(1, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "%run test.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# %load test.py\n",
    "def f(x, y, z):\n",
    "\treturn (x + y) / z\n",
    "\t\n",
    "\n",
    "a = 5\n",
    "b = 6\n",
    "c = 7.5\n",
    "\n",
    "\n",
    "result = f(a, b, c)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "%run test.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4666666666666666\n"
     ]
    }
   ],
   "source": [
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.4666666666666666"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "c = np.random.randn(100, 200)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.51759491,  1.5054886 , -0.85397219, ..., -0.60192617,\n",
       "        -0.19998038,  0.16021563],\n",
       "       [-1.22081324,  0.46086494,  0.24612417, ...,  1.37789708,\n",
       "        -1.21439607,  2.67276055],\n",
       "       [-0.58929068, -0.80779362, -0.97430662, ...,  1.22895871,\n",
       "         0.4086862 ,  0.03114983],\n",
       "       ...,\n",
       "       [ 0.12865538,  0.6492206 ,  0.84466922, ...,  2.54044259,\n",
       "        -1.2172077 , -1.06982229],\n",
       "       [-0.71496733,  0.74575881, -2.39148574, ...,  1.17850348,\n",
       "         0.87083106, -2.66207848],\n",
       "       [ 0.46115756,  0.22512114, -2.4179148 , ...,  1.91228744,\n",
       "         1.22002441,  2.16254289]])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "shapes (100,200) and (100,200) not aligned: 200 (dim 1) != 100 (dim 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-22-78b87256aca3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mget_ipython\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun_line_magic\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'timeit'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'np.dot(c, c)'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mD:\\ProgramFiles\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\u001b[0m in \u001b[0;36mrun_line_magic\u001b[1;34m(self, magic_name, line, _stack_depth)\u001b[0m\n\u001b[0;32m   2325\u001b[0m                 \u001b[0mkwargs\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'local_ns'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_local_scope\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstack_depth\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2326\u001b[0m             \u001b[1;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbuiltin_trap\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2327\u001b[1;33m                 \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2328\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2329\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<decorator-gen-54>\u001b[0m in \u001b[0;36mtimeit\u001b[1;34m(self, line, cell, local_ns)\u001b[0m\n",
      "\u001b[1;32mD:\\ProgramFiles\\anaconda3\\lib\\site-packages\\IPython\\core\\magic.py\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(f, *a, **k)\u001b[0m\n\u001b[0;32m    185\u001b[0m     \u001b[1;31m# but it's overkill for just that one bit of state.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    186\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mmagic_deco\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 187\u001b[1;33m         \u001b[0mcall\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mlambda\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    188\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    189\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mcallable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\ProgramFiles\\anaconda3\\lib\\site-packages\\IPython\\core\\magics\\execution.py\u001b[0m in \u001b[0;36mtimeit\u001b[1;34m(self, line, cell, local_ns)\u001b[0m\n\u001b[0;32m   1167\u001b[0m             \u001b[1;32mfor\u001b[0m \u001b[0mindex\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1168\u001b[0m                 \u001b[0mnumber\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m10\u001b[0m \u001b[1;33m**\u001b[0m \u001b[0mindex\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1169\u001b[1;33m                 \u001b[0mtime_number\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtimer\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimeit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnumber\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1170\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mtime_number\u001b[0m \u001b[1;33m>=\u001b[0m \u001b[1;36m0.2\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1171\u001b[0m                     \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\ProgramFiles\\anaconda3\\lib\\site-packages\\IPython\\core\\magics\\execution.py\u001b[0m in \u001b[0;36mtimeit\u001b[1;34m(self, number)\u001b[0m\n\u001b[0;32m    167\u001b[0m         \u001b[0mgc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdisable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    168\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 169\u001b[1;33m             \u001b[0mtiming\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minner\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mit\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    170\u001b[0m         \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    171\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mgcold\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<magic-timeit>\u001b[0m in \u001b[0;36minner\u001b[1;34m(_it, _timer)\u001b[0m\n",
      "\u001b[1;32m<__array_function__ internals>\u001b[0m in \u001b[0;36mdot\u001b[1;34m(*args, **kwargs)\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: shapes (100,200) and (100,200) not aligned: 200 (dim 1) != 100 (dim 0)"
     ]
    }
   ],
   "source": [
    "%timeit np.dot(c, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using matplotlib backend: Qt5Agg\n"
     ]
    }
   ],
   "source": [
    "%matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2af192f6a00>]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXIAAAD4CAYAAADxeG0DAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAA7Y0lEQVR4nO3deXxb13Uv+t/GPBIgCHCeKWqgLGswJduSHcdT7CRuHCvz8DL2Obltep3XpmlSt02avnR4Tl/ubZre1ml7EydpbGdw47hJPCbyINmWLImyRIoURXESBxAgQYAAAWLY9w/ggBNATAfDAdb38/HHFolhH0tc2lhnrbUZ5xyEEEKkS1bsBRBCCMkNBXJCCJE4CuSEECJxFMgJIUTiKJATQojEKYrxplarlbe3txfjrQkhRLLeeOMNB+fctvHrRQnk7e3tOHXqVDHemhBCJIsxNpbo65RaIYQQiaNATgghEidKIGeM/TtjzM4YOy/G6xFCCEmfWDvy7wK4W6TXIoQQkgFRAjnn/EUA82K8FiGEkMwULEfOGLufMXaKMXZqbm6uUG9LCCFlr2CBnHP+MOe8l3Pea7NtKoMkhBCSJUlVrZwcncc//Xa42MsghJCSIqlA/uvzM3jo6UGcGV8o9lIIIaRkiFV++CMAJwDsYIxNMsY+LcbrbvT5O7pRa1Tjz/7zPMIROhCDEEIA8apWPsQ5b+CcKznnzZzzfxPjdTcyapT483t6cGHKjR+8mrBTlRBCKo6kUisA8M49Dbi524pvPD0Iu8df7OUQQkjRSS6QM8bwtXuvQSAUwdf/a6DYyyGEkKKTXCAHgA6rHp99axd+fnYKx4cdxV4OIYQUlSQDOQD83lu70GrR4c9+fh4roUixl0MIIUUj2UCuUcrxl/fuxsicF995aaTYyyGEkKKRbCAHgFt31OLu3fX41guXMDHvK/ZyCCGkKCQdyAHgL36nBzLG8Je/uFDspRBCSFFIPpA3mrX4b7d04bkBO+3KCSEVSfKBHAD2tpgBADNuqisnhFSesgjkNqMaADDnCRR5JYQQUnhlEchrY4HcTjtyQkgFKotAXq1TQS5jmFuiHTkhpPKURSCXyRisBhXsbgrkhJDKUxaBHABqjRrakRNCKlLZBHKbUU03OwkhFalsAnmtUQ07BXJCSAUqm0BuM6rhXArQyUGEkIpTNoG81qhGhANOL+3KCSGVpWwCOTUFEUIqVdkFcsqTE0IqTdkE8lqjBgDtyAkhladsAjmlVgghlapsArlGKYdRo6BATgipOGUTyIHortzuocFZhJDKUlaBvJa6OwkhFaisArnNqKFATgipOGUVyKlNnxBSicoqkNuMavhWwvAGQsVeCiGEFEx5BXJD+k1BP3p9HAPT7nwviRBC8q6sAnltVXq15CuhCB584k08cmKsEMsihJC8KqtAvtqmv3UJ4vi8DxEOzCwuF2JZhBCSV6IEcsbY3YyxQcbYMGPsS2K8ZjbSbdMfdXgBANOLVHNOCJG+nAM5Y0wO4NsA3g6gB8CHGGM9ub5uNsxaJRQyljJHPuqMBvIpF+3ICSHSJ8aO/BCAYc75COd8BcCjAO4V4XUzJpOxtI58EwK52x+iChdCiOSJEcibAEys+fVk7GvrMMbuZ4ydYoydmpubE+FtE0snkI85ffH/pvQKIUTqxAjkLMHXNp23xjl/mHPeyznvtdlsIrxtYjZD6qagKw4v6qui+fQZCuSEEAChcKTYS8iaGIF8EkDLml83A5gS4XWzUlu19Y48EApjyrWMw101AIApqlwhpOIt+oLo/fpz+OT/fl2SmzsxAvlJAN2MsQ7GmArABwE8KcLrZsVmUMPpDST923VifhkRDlzfaQEATLuk95tGCBHXy8MOuHxBvHTJgTu/eQw/PjUBzqVzkHvOgZxzHgLwOQBPAxgA8Djn/EKur5stW5UGnAPz3pWE3xdKD7vrjLAa1Jhx046ckEp3bMiOKo0CT/8/b8Gu+ir88U/O4VPfPSmZ3bkodeSc819yzrdzzrs4518X4zWzlapNX6hY6ajRo8GkwRTtyAmpaJxzHBuaw83dNnTZDHj0/hvwld/pwYkRJ+785jE8LoHdeVl1dgKp2/RHnV6YtEpU61VoMGkwTTlyQira4KwHs+4AbtkeLcKQyRg+eaQDv34gujv/4k/O4Z9+e7nIq9xa2QXy1R154p32qMOH9hodAMQCOe3ICalkxwaj5dBv2b6+mq7dqsej99+A7loDzowvFGNpaSu/QJ7iEOYrDi/arXoAQINZC48/hCVqCiKkYh0bmsPOeiPqTZpN35PJGKwGNRaXg0VYWfrKLpBrlHJUJTmEORAKY2pxGe01sUBuEmrJKb1STOEIhz8YLvYySAXyBkI4OTofT6skYtYp4fJRIC84W5KTgibmfeAcaLcKqRUtANANzyL7618O4Pa/P4ZIpLRvKJHyc+KyE8Ew3zKQm7RK2pEXQ22SsztHHdHW/I07crrhWTyOpQB+8OoYrrqWMTBDB32Qwnrx0hx0Kjmua69O+hgK5EWSbEceLz2M5cjrqjRgjOatFNMjJ8YQCEWbt05cdhZ5NaTSHBuaw+GuGqgV8qSPMemUCIQiJZ3+K8tAXhsbnLWx9vOKI1p6aNapAAAqhQxWg5q6O4vEtxLCIydGcceuOnRa9RTISUGNOrwYc/o2VatsZNIqAaCkd+VlGchtRjWWg+FN1ShjTl+8YkXQaNJg2k2BXEyhcCStBoofn5qEyxfEZ2/pxI1dNXjtyrykBxcRaTk2FC073Co/DlAgL5pkJYhXHF50xGrIBfUmDabpgAnRhMIR3PR3v8Ff/3Ig5eO+89IIDrSa0dtuweEuK5YCIbx5dbFAKyWV7tjQHNprdGir0W/5OLM2+gmeAnmBCUe+rc2T+4PR0sONv2kNJi3lyEU0OOvBjNuP77x0Bc/2zyZ93K/Oz2ByYRmfuaULAHBDbIjZcUqvkALwB8M4cdmZcjcOrO7IS7kEsSwDeaId+eRCtPSwY2NqxazBUiAEj790f5Ok5OyECwDQatHhj3/Sl7AiiHOOf3nxMjqtety5qw4AUGNQY2e9kfLkpCBOjS5gORjGLTvSD+S0Iy+w2gSB/IpQerghkNfHaslpVy6OM+MuWPQqfPeTBxEMRfDAj85uynufuOzE+atu/N9v6YRMtnouyY1dNTg5Oo9AqHSrA0h5ODZkh0ouww2dNSkfS4G8SMw6JZTy9YcwC+Nr2zfkyBtjteR0ELM4zk64sL/FjE6bAX/17mvw+ug8vvXC8LrH/POLI7Aa1Lhv//oTAQ93WREIRXBm3FXAFZNKdGxoDoc6LNCpFCkfa9QowBiw6Es8GrsUlGUgZ4zBZlh/UtCo0wuzbrX0UNBgju7IpTJ3uJQtLgcxbF/CvhYzAODogWYcPdCEb71wCa+ORFMmA9NuvDg0h08eaYdGub5291CHBTJGeXKSX1OuZQzNLqWVHwei81aqNKXdFFSWgRwQmoJWg/Oo0xvv6Fyr1qgGY8AUBfKcnZt0AQD2t652yf3VvdegrUaPzz96FvPeFTz84gh0Kjk+en3bpuebtErsaTLhxGVHoZZMKtBLl2Jlh2nkxwWl3t1ZxoF8fZv+2vG1aynlMtQa1TQ4SwRnx11gDLi2xRT/ml6twLc+tB/z3hX8tx+8gV/0TeGDB1th0ikTvsaNXVacnXDBt0ITKUl+HBuaQ32VBt21hrSfY9Yp4aJAXng242pqRSg93HijU1BPJYiiODPhQpfNgCrN+iB9TZMJX3r7Trx2ZR4cwKdv7kj6Goe7ahAMc5waLe35z0SaQuEIXrrkwC3bbWCMpX5CTKnvyFNn+iXKZlRj3reCYDgSn3q4sfRQ0GjSYGjWU+AVlhfOOc5OuHD7ztqE3//kkXZcnltCjV6Fpth9iUR626uhlDMcv+xM2TpNyt/04jJOjS7g3KQL79jTsC5tl41zVxfh8Ycy/rNVpVXiagkXRJRtIK81qsE54FxawagzWnqYrIOrwaTFsaE5cM4z+luarBqf92Heu4J9reaE32eM4ev37Un5OjqVAvtbqilPXqGG7R4cv+zEqdEFvDG2sC54zroDOQfy8Vgs2NlgzOh5Jq0SbtqRF97apiCh9LAjaSDXwLcShtsfiteMkswIjUD7W3L7QQOi9eTfeuESFpeD9PtRQSbmfbjzmy+Cc6CuSo3eNgs+fVMHetur8de/HMD4vC/n95iNzVUSek3SZdZGD5co1c1e2QZy4TfK7vHjitOLap0y6Q22BrNwUpCfAkeWzoy7oFXKsb0u/RtIyRzuqsH/fP4SXr8yjzt76kRYHZGCV4Yd4Bz4yWdvxHVt1esCZofVgKcvzOT8HrPuAHQqOQzqzEKfSatEKMLhWwlDn+FzC6Gsb3YC0R35mNO75WAc4YCJKapcydqZCReubTZBIc/9j9S+VjPUChmOU3qlohy/7ITNqN4UxAGgrUaHee9KzqM07B5/rOQ4s111qXd3VkQgH3X4kt7oBFaPfKO55NnxB8Pon1pMmh/PlFohx8F2C81dqSCcc5wYceLGzpqEQbbNEi0dHnPmll6xuwOordp8yHIqZl1pD84q20CuVshh0ioxseBbd+ByIrVGNWQsu0OY3f4gvv2bYQQreI52/7QbwTAXJT8uuLGrBhdnPHAsbT7piZSfy3NLmPMEcLgr8eyT1lgPSK55crvHj7osAnkV7ciLx2ZU442xhXUHLieikMtQa9Rk1d35y3PTeOjpwYquexZmo+wXaUcOIP4DLbT2k/ImfPq6MVkgF2FHzjnHrDuQ8Y1OgFIrRVVrVOPynDAsa+vh8Q1mTVaHMF+cidafjziWMl9gmTg74UKjSZPVTieZPU0mGNQKSq9UiOOXnWgya+MBeyOjRgmLXpXTjtwTCGE5GEZdVeaBXJjRtLhcmoOzyjqQ29b8zZsqkDdm2d15MXby+2W7N+Pnlosz4wui5ccFCrkM13dQnrwSRCIcr444cUOS/Lig1aLD+Hz2P2d2dzRNl82Gg3bkRSR8hNqq9FAQPfLNn9ZZkwLOecXvyB1LAUwuLIuaHxfc2FWDEYcX9/7jy/jKz8/jiTOTGJlbyuj3iJS+izMeLPiCSfPjgrYaXU6pFXushtyWRWpFr5JDLmMlG8hLryBSRMJvWLIZK2s1mDRYDobhXg6lDPoCuycAly8IGQNG5ipzR342lh8Xe0cOAO+7rgVO7wpOjy3gx29M4nsnxgBEd0f7W834wtt24JomU4pXiTozvgAZY9jbIv46SW6EMtNk+XFBm0WHX/RNYSUUgUqR+R50NjYNNZsdOWOspOet5BTIGWPvA/BVALsAHOKcnxJjUWIRzu5M1tG5llCCOLW4nHYgH5iOplUOdVjw+pV5+IPhTTO2y92ZiQUoZAzXNKYXUDNh0inxJ3fvBACEIxyX7B6cHXehb9KF5wbseP+/nMC3P3IAt+5IPN9F8N1XruBrT/WjqVqLl754m+jrJLl5dcSJ9hodGreYwQMArTV6RDhw1bW8ZTlxMkJqJZubncBqd2cpyjW1ch7AUQAvirAW0Qk78lSnZAOr3Z2Z3PAU0irv2NOACM+9xlWKzk64sLPBCK0qv3+ByWUMO+ur8MFDrfibo9fiqT+4CR1WPX73e6fw6OvjCZ8TCkfwFz8/j6/+oh+1Rg0m5pfjszZIaQiFI3htZB43dllTPratRqhcye7Tb7ZdnYKqEt6R5xTIOecDnPNBsRYjtlaLDowBPY1VKR/bmMXZnRen3WgwaXAgNshnZK6y8uThCEffxGJe8uOp1FVp8NhnbsRN26z40s/exN8/M7gud+72B/Hp753CIyfGcP9bOvHIpw8BAF4epm7RUnJhyg1PIJQyrQKsliBmW7ki1JBnOyullAdnFexmJ2PsfsbYKcbYqbm5uYK8Z4tFh99+4a24Y9fWH72B6O5dLmMZdXdenPFgR70x/jFvxFFZefLLc0tYCoTiR7sVmkGtwL9+vBcfPNiCb70wjD96vA8roejY4vf+r+N4ZdiBvz26B3/6jl3orjWgvkqDVyiQlxThWL8b0zgEudaohkYpy/pTld0dyOpGp6CUD5dI+RmDMfYcgPoE33qQc/7zdN+Ic/4wgIcBoLe3t2BlB+mkVYDoR/c6ozrtHflKKILLc0t4645a6NUK1FdpcNleWTvyM+PRJigxG4EypZTL8DdH96C5WotvPDOEyYVlXJ5bQjAcwSOfOoTD26If2RljOLytBr+5aEckwiGTld4Eu0p0YsSJ7lpDWgGWMYZWiw5jWe7IZz1+XNtszuq5QGkfLpEykHPO7yjEQkpBg1mbdo58xLGEYJhjV2yucVetHpcrbEd+dsIFk1aZ1Y0nMTHG8LnbutFo1uKLPzmHpmot/v0TB9FlWz+J8aZtVvzs9FX0T7vTrnYh+bMSiuDklXm8v7c57ee0WvRZ7cg559E5KznsyIXUSiluBMq6/DBT9SYN+qfcaT12MHajc0d9NJB3Wg34z7NXS3ZecT6cGXdhX4u5ZK736IFmXNdWDYteBaNmc+XRkdju/JVhBwXyEnBu0oXlYDit/LigrUYXG3eb2c9ZLl2dApNWiQiPvlapjbvOKUfOGLuPMTYJ4EYA/8UYe1qcZRVHoynapp9Ow8nAtAdKOUOnNbrr67Tp4fGHMFchQ568gRCGZj1Fy48n01ajTxjEgegN0u5aA93wLBHHLzvBGHB9R2aBfDkYXnewejpy6eoUCMG7FG945lq18gTnvJlzruac13HO7xJrYcVQb9LCH4ykVSt6ccaNLpsh3pggfIyvlMagh54eRISnbuIoNUe2WXFydB6BULjYS6l4xy87sKu+CtV6VdrPaRGGZ2WYJ8+lq1NQym36Zd2in6nGDA6YGJzxYFfDalljpy1WuVIBgfz7r47hu8dH8bs3deCGNKoNSsmRbVb4gxGcHnMVeykVzR8M4/S4K2Vb/kbCXPJM8+S5dHUKKJBLREOss2wmReWKy7eC6UV/PD8OROvQNUpZ2deSv3RpDl998gJu31mLL79jV7GXk7HrOy2QyxiVIRbZ6bEFrIQiOLwts0DeXK2DjGWzI889tSJMQCzF7k4K5GusHvm2dSAXOjp3rgnkMhlDe40el8s4kA/bl/B7PzyN7loD/ueH9kNeYnfu01GlUWJvswmv0DFyRXVixAm5jOFguyWj56kUMjSYtBjPsLsz165OgHbkkmE1qKGQsZQnBV2MzVhZm1oBgK5aQ9k2BS14V/Dp752EWiHDv368N6cfiGI7ss2KvgkX3Dme/0iyd/yyE3uaTElvTG+lrSbzWvLZLE8GWosCuUTIZQx1VZqU3Z2Dsx6YdcpNNaldVj0m5n1ldyNtJRTBZ37wBqYX/Xj4Y71ork5+2pIUHNlmRYQDr9Ks86LwBkLom3BlfaO8rUaXcY58LseuTgDQKGVQKWRwleDhEhTIN2g0a1LuqgemPdhZb9xUx9ppM5Td8CzOOR584k28fmUeD7332vhcGSnb32qGVimnPHmRPDcwi1CEp9WWn0irRQ+ndwVLgVDazxFjRy6Msi278sNydOvOWpydcGE4Sbt9JMIxNOvBzvrNg7hWSxDLJ0/+1Llp/PiNSfz327tx776mYi9HFGqFHIc6LHiFduQFN724jK88eQE9DVVZVzytnt+ZXhpT6Oqsy3FHDpRumz4F8g3ed10LlHKGHyUZjTqx4INvJbzuRqegI1aCeLmMShCf7JtCo0mDz9/eXeyliOrIthoM25dSVigR8YTCETzwo7NYCUXwjx/en9XhEMDqONuJNPPkQldnbQ5dnQJTic4kp0C+gc2oxl276/GTNybhD27OdQ9MxypWGjbvyA1qBeqq1GVTS768EsZLl+ZwZ09dyc2WyNXadn1SGP/w/CW8PjqP//fd16BzwxycTLTG55KnF8iFZiAxDgc3045cOj5yfRsWl4N46tz0pu9dnHGDMWB7XeI/iJ1WQ9mUIL487IA/GMGdPYmGX0rbrvoqWPQqKkMskOPDDnzrN8N4z4FmHD2Q/pCsRKo0SlTrlGlXrqyeDJR7IKfUioTc0GlBl02PH742tul7gzMetFl00KkSl9911erL5oDgZ/tnYNQocH1nZrW+UiCTMRzuqokPYCL541gK4IHHzqLDqsfX7t0tymu21qQ/BVHo6hQjtVKqpwRRIE+AMYaPXN+GM+MuXJhaXPe9izOJb3QKOq0GuP0hOL2lV6KUiXCE4/kBO27dUQulvDz/mBzZZsWsO1A2n6BKUSTC8YeP92FxOYhvf/gA9CL1H7RZdBibTy+FKUZXp8CsU8LjDyEcKa2//MvzJ1QE7znQDLVChv94bfWmp28lhFGnFzsbNt/oFAgzV6R+yMTp8QU4vSu4s6eu2EvJm5tiefKXL1F6JV8efmkELw7N4c/v6dnUQJeLthodplx+BMORlI8Vo6tTUKoTECmQJ2HSKfE7exvxn2euxutVh2aXwDm23JHHSxAl3uH5bP8slHKGt+6wFXspedNi0aHVoqMyxDw5O+HCN54exNuvqcdHr28V9bVbLDqEIxxTrtQD7sSoIReUancnBfItfOT6VnhXwvj52asAgMGZaGt+otJDQZNZC7VC2sOzOOd4tn8WN3TWZNVCLSVHttXg1cvOsuvGLQWPn5qAVinH377nWtEPH2mzpF+5MpfjyUBrCYG81M7upEC+hX0tZvQ0VOEHr46Dc46BaQ+0Snm8ISERmYyhw6qXdC355bklXHF48bYyTqsI7tpdD08ghN9cLMyB4JVk1OFFV60hL6fpCGfxplO5Muvxo1akHblZRztyyWGM4aM3tGFg2o0zEy5cnHFjR70xZU11p00v6R35M/2zAIA7KiCQ37TNCqtBjSfOTBZ7KWVnzOnL23mutUY11ApZyimInHPMuv2idHUClFqRrHfta4RBrcAPXh3D4Ixny7SKoMtmwMTCMlZCqW/ElKJn+2exp8mEBpO22EvJO4Vchnv3NeKFi3YsSLzSqJT4g2FMLS7HuzDFJpMxtFp0KVMrnkAI/mBEtBx5lRDIfaX1Z4UCeQoGtQLv3t+IJ89OYcEXTCuQd9r0CEc4xtMsjyoldo8fZydcZV2tstHRA00IhjmeenNzAxjJzsS8D5wD7TX52ZEDsSmIKVIrQlenGDXkAO3IJe3Dh9oQitWNJmrN30g4kHnYLr1A/vyAHZyjogJ5T0MVdtQZ8cRpSq+I5Uqsaqs9T6kVIDoFcXzet2VDl5hdnUB04JpWKadALkU9jVU40GoGsHXFiiB+fqdDennyZ/tn0VytTes6ywVjDPcdaMLpcVc8AJHcCCmP9jylVgCg1aKFbyUMx1LyNIeYXZ2CUmzTp0CepgffuQt/cNu2+Ll9WzFqoodOSG14ljcQwsvDDrytp170crFS9+59TWAMeOLM1WIvBWNOLw7/zfOS/ktl1OmFSatM6+clW0LlylYpzFkRuzoFZl3pTUCkQJ6m69os+KO37Uj78Z224p3f6Q+GcdPfvYCfZZgqeOnSHFZCkYpKqwjqTRoc6bLiiTOTRZ+98uIlB6YW/ZvGQ0jJqNOb17QKkN4URLs7AL1IXZ2CUpy3QoE8TzptBozMeYsSFIZmPZhcWMbDL45k9P7PXJiFWafEwXbpnwKUjaMHmjAxv4xTYwtFXUffhAsA4PAEirqOXIw6fHlNqwBAc7UWjG0dyMWsIRdQaqWCdNkMWFwOYn5NSdus248n+6bw1Scv4NhQ/hpQ+qeiHagXZzx482p6u7pQOIIXBu24bUctFGU6JCuVu3bXQ6uU42eni5teiQfyLXK/pSwQipYe5rNiBYjeeGw0abesXBGzq1NQioFcukehlzjhhue/vnwFzqUAXrsyv27n8LPTk3j2D28RNXcn6J92Q6eSI8I5Hj05gWubzSmfc3J0AS5fsCLTKgK9WoG7r6nHU+em8JXf6YFGKS/4GpYCIQzHUnKOJWnuyOOlh9b8H9LdatElPZYRiO7I96bx5z8TpXi4RGVuvQpge1206uN//fYynumfxfY6I/7snbvwi8/dhOf+8C0IhCL405+9mZfUS/+UG7sbq/COPQ34xdkp+FZSH1L7q/PTUClkeMv28h2SlY6jB5rg8YfwwkV7Ud7/zclFCH8kpBrIRx3RDUtbnnfkAHDzdivevLqY8Maw0NWZjx25byVcUg1/FMjzpMmsxaP334Bff/5mnP6zO/Gdj/Xid2/uxJ5mE7bVGvHHd+3A8xftoldJRCIcA9Nu9DRU4QO9LfAEQvjlmzNbPmd6cRmPnpzAu/Y2ijYvWqoOd1lRV6UuWnqlb9IFANjTZMKcRHPko7G2+Y4CBPL3HmiGXMbw+KmJTd8Tu6tTYCrBeSsUyPPohs4a7KyvSjib5ZNHOtDbVo2vPnkBs27xDgAen/fBuxJGT2MVDnVY0GHV47GTiQ+SFvzD88PgnOOBMjtgORtyGcO9+5rw20E7nEXYEfdNuNBWo0N3rUGyOfJRpxdVGkV8wFQ+1VZpcOsOG376xiRCG2aTi93VKSjF7k4K5EUilzE89L69WAmLm2Lpn47e6OxpMIExhg8cbMHJ0YWkpZCjDi8ePzWBDx9qRcsWUx0rydEDTQhFeMIzW/Otb8KFa5vNsBnVmFsKFL0UMhvCsKxC9SK8v7cFdk8Avx1cX0AwK3JXp4ACOVmnw6rHH9+1E89ftIv2Ub5/yg25jKE7djj00QNN0Y+eJzd/9ASAbz43BJVcht+/bZso718OdtZXYVdDFX5W4OYgu9uPqUU/9jabYDWosRKKwBNIfX+j1FxxeAuSHxfcurMWVoN6U3rFHuvqrMvTjryUTgnKKZAzxh5ijF1kjJ1jjD3BGDOLtK6K8cnD7TjYXo2//IU4KZaBaTe22Qzxiotaowa376zFT09PbjoWa2DajSf7pvDJI+2i71qk7uj+JvRNuNI+4FcMfZPRUtF9LWZYjdGOSKnVkgdCYUy5lvNeQ76WUi7Dew404YWL9nX3FeI78jzUkQOAa7l0Ul+57sifBXAN5/xaAEMAvpz7kiqLTMbw0HujKZYvi5Bi6Z92o6dx/WCvDxxsgWNpBc8PrK/E+PtnhmBQK/CZt3Tl9J7lqDfWFHXJ7inYe56bdEEuY9jdGN2RA9KrJZ9cWEaE53dYViLv621BKMLXdTPno6sTQHzswGIJtennFMg5589wzoXPfq8CaM59SZWn3arHF+/aiRcu2vHTHFIs894VTC/60bNhQuMt222oq1Kvu+l5enwBzw3M4rO3dMXvwpNVTdXRWexX0zgTUixnJ1zYUWeEViWPB3KpVa6MxsoAC5laAYBttQb0tlXjsVMT8c2QmGd1rlWlif7FsLhcOmkvMXPknwLwq2TfZIzdzxg7xRg7NTdHx2pt9InD7ehtq8bf/upi1vWpA8KNzg07coVchvdd14JjQ3OYXlwG5xwP/XoQVoMKnzjcnuvSy5JVr4ZKIcPkQmECOeccfRMu7G0xR98/viOXWCCPpaLydTLQVt5/sAUjc168ERuxYHf7YRO5hhyI/jwZ1ApppVYYY88xxs4n+OfeNY95EEAIwA+TvQ7n/GHOeS/nvNdmq+ymk0RkMoY/uL0bjqUAfnU+u2oJoTV/V4KZ6e/vbUGEAz85NYlXhp04MeLE79+6reLrxpORyRiazVpcLVAgH3X64PaHsLfZBACw6FWQMQkGcocXRo0C1UX4lPfOPQ3Qq+R4LHZj3+4J5GVHDpRem37Kn2LO+R1bfZ8x9nEA9wC4nUuxVqqE3LzNig6rHo+cGMO9+5oyfn7/tBv1VRpY9JtHh7bW6HC4qwaPnZrAcwOzaDJr8eHrW8VYdtlqqtZiskCpFWG+irAjl8sYLHq19AK504v2msKVHq6lVytwz7WN+MW5KXzlXbvz0tUpMGmVZVW1cjeAPwHwLs554W7vlymZjOH/uqENb4wt4Hyaw67W6p/afKNzrQ8cbMHkwjL6JhfxwB3dUCsKP0tESpoKuCPvm3RBq5Sju9YQ/5rVoMKcp3Q+vqdjzOkr+I3Otd5/sAW+lTAefX08L12dApO2tGaS55oj/0cARgDPMsbOMsb+WYQ1VbT3XNcMnUqOR06MZvQ8fzCM4bmlTTc617prdz1MWiU6bXoc3Z/5jr/SNJm1cCwF4A+G8/5efRMu7GkyrZs8aTNKa0e+EopgciH/42u3cqDVjG21BvzLiyMAxO/qFJh1pZVaybVqZRvnvIVzvi/2z2fFWlilMmmVuG9/E35+diqjU90vzS4hHOFb7sg1Sjm+96lD+M7Heit2VG0mhMqVqTynV4LhCM5PubG3xbTu61aDWlJVK5MLvmjpYYErVtZijOEDvS3x/2/56o8otRw5/TSXoI/d2I5AKILHEgwCSqZ/OpqK2WpHDkSbTbpshi0fQ6KazNFAnu/KlcEZD1ZCkXh+XGA1qOCQUJu+MCyrEONrt3LfgSYoYvONxO7qFFAgJyntqDfihk4Lvn9iDOFIej/EA9Me6FVytNK8FNE0x/5f5ruW/Kxwo3PD3GyrQY1AKIIlibTpF3J87VasBjVu31ULQPyuTkGVVolAKFKQtFs6KJCXqI/f2I6rruW052L3T7mxqyHxpEWSnTqjGnIZy/sNz74JFyx6FZpjqRyBUAMtle7OMacXRrUCNQmqpgrtS2/fha/du1v0rk6BucRG2VIgL1F39tShwaRJ66ZnJMITtuaT3CjkMtRXafK+Iz83uYi9zaZNJXuZNAX9/g9P429+OZCX9aXritOHNquuKKWHG3VY9fjYje15e/1Sm4BIgbxEKeQyfPSGNrx0ybHlUVZANIe7FAilzI+TzDVV57cEcSkQwpDdsyk/DqwJ5Gnc8HzlsgOvjjjFXl5GxmI15JUgPjirREoQKZCXsA8cbIFKLsP3U+zK4zc6aUcuumazFpML+WuROH81erRbwkAem4A4l2JHvrgchMsXLNg4gUSC4QgmF/J/4HKpMGtjg7NoR05SsRrUuOfaBvzkjUl4/Mn/wAgzyIVzQol4mqq1mHH7N40AFktfkhudAGDRqcBY6h35ROwUead3Bd4i3RidXFhGOMLRVsQa8kKi1ArJyMcOt8O7Et7ybM/+aTe6bPqinPpe7pqrtYhwYGZRvOP41uqbdKHFok04VkEhl8GiU2Euxc3O8fnVTwyFnNa4VvycziJ2dRbSamqlNG5EUyAvcftazNjbbMJ3j48mnYooVKwQ8TWZ81uC2DexmHA3Lkinu3NtIM9nGmgrxRpfWyxGjQKMlc4pQRTIJeD3bt2GkTkvvvDjPkQ21JUveFcwlWAGORFHfC55HvLPc54ArrqWsS9BflxgNaQXyJXyaKXIxHxxduRjTh8MagWshuKXHhaCTMZQpSmdpiAK5BJw1+56/MndO/Fk3xS+9lT/uk6/ZDPIiTgaTNGGknzcSDw36QKQ+EanQOju3MrEvA+7GqqgVsiKtyN3etFWUxqlh4Vi0irhKpFATsOoJeKzt3TCsRTAv718BVaDCp+7rRtAND8OJJ5BTnKnUcphM6px1SV+gDw7IRztlvz3Tpi3wjlPGiTH533Y02SCNxAqWuXKqMOL3Y2m1A8sI6XUpk87colgjOHBd+zCffub8I1nhvCj16PHtvVPu1FXpY7XHBPxNZm1ecmRnx5fwM56I3Sq5Pspq1ENfzAC70riVvBQOIKrC8totejQYtFhogg78njpYZFnrBRaKU1ApB25hMhkDP/fe6/Fgm8FDz7xJqp1yugMctqN51VztTar+fBbCUc4+iYWcV+KccJrm4IStZtPL/oRinC0WnRw+4PxuS2FdHVhGaEIr5gbnYJqnQr9U24sLgfjVSzFQjtyiVHKZfinjxzA3hYz/vujZ3HJvkT58TxrqtZiyuXfdKM5F5fsHiwFQtjfat7ycavzVhLnyYUa8laLDs3VOrh8wS17DvKh0koPBR+7sQ2Ly0H84WNnRf2zkQ0K5BKkUynwvz9xEG0WXXQGeUNl5SYLrdmsxUo4IuohD2fGXQCAA63VWz5OqAJJ9t5C6WGLRYeW6mhqo9B58jGnMPWwslIrve0W/Pk9PXj+oh3/8MKloq6FArlEmXUqPPLpQ/jE4XbcvN1a7OWUNaEEcULEAHl6bAEWvSpl8LPFUivJmoLG531QyBgaTJr49MRCB/IrDi/0Knl8rZXkYze24eiBJvyP5y7h+YHZoq2DArmENZi0+Oq7dqNKU9z8XLnLR1PQmQkX9reYU5brWfTRNv1kJwWNz/vQVK2FQi6LB/KJ+cLe8IyWHhbnwOViY4zhr+/bg92NVfj8Y2dxJdYYVWgUyAlJQeymoEVfEMP2pZT5cSDapl+tS15LPjHvix8mYtGroFPJC74jH5zxoLuuck+d0ijl+OePXgeFjOEz3z9VlHk3FMgJScGgVsCsU4pWS3421giUKj8usBpUSQdnja0J5IwxNFfnd1rjRvPeFUwv+resha8ELRYdvvWhAxi2L+GLPz1X8OP5KJATkoYms3hzyU+PLUDGgGu36OhcK1mbvjC+du3xfs3VOlFz+an0T0Ub0iqtGSiRm7qt+OLdO/Ff56bxnZdGCvreFMgJSUOTWStayuLMhAvb64xpH0MWHZy1+Wbn2tJDQUuBd+QXptI79LtSfOYtnbh7dz3+7teDBW0WokBOSBqaqqPdnbl+ZI5EOM6ML2B/mmkVIPmOfGJN6aGguVoHjz9UsCByYcqNRpMG1SVwTmcpYIzh6IEmhCMcY87C3fikQE5IGprMWvhWwjkf7XV5bgkefwgH0rjRKbAa1PCthDfdRBNqyFtr1gbywlauXJhaRA+lVdYRfj/GC1g9RIGckDQIATLXEkShESizHXnipqDxeR/MOuW68lNhd16IyhXfSggjDm/F3+jcSGjMokBOSIlpFqlr8vT4AkxaJTozaGe3JmnTH19TsbK6TqEpKP9BZGDaA85BgXwDfWwu+7iTAjkhJaXJLE6APDPuwr4WM2Sy9Jtn4t2dnvU3PCfmfevy40B0tKpBrSjIjrw/dqNzdxOlVjZqtehoR05IqTHrlNCp5DmlVtz+IIbsnrTrxwWJBmeFIxyTsfG1axWylvzClBtmnRKNscM3yCoK5ISUIMZYzrXk5yYWwTlwoM2c0fOEg5nXBvLpxeX4+NqNmqt1KY98C4TCeG3EmdE6Nrow5cbuxqqKbM1PpdWiw5RrGcFw4nN2xUaBnJA0CSWI2To9vgDGtj7aLRGlXIZqnXLdvJXxBDXkAmFHvlWp5PdPjOEDD7+adXVLMBzB4IyHGoGSaLHoEOH5Oes1EQrkhKQp15OCzowvoLvWkNWQs4215ImagQQtFh28KUolX7zkAAAMzy1lvBYAGLYvYSUcoRudSQiHbBQqvZJTIGeM/RVj7Bxj7Cxj7BnGWKNYCyOk1AgHNyxlMRSJcx6beJhZflwQDeSrNzvXjq/dvE5h7G7iIBIIhXHyyjwAYGQuu6aVC/HWfArkiQh/wUoikAN4iHN+Led8H4CnAPxF7ksipDTlMgXxisMLly+YcX5cYDWu35GPzy/Hx9dulGou+ZlxF5aD4di6stuRX5hahFYpR4e1cqcebqXWqIZKIStYY1ZOgZxz7l7zSz2A4p53REgeCSWI2UxBPJ1FI9BaNoN63QTERDXkgtWa98TrPD7sgIwBXTZ91vOzL0y5sbPBCHkGZZSVRCZjaKnWSmZHDsbY1xljEwA+gi125Iyx+xljpxhjp+bm5nJ9W0IKrjmHHfmZ8QUY1Qpss2W3g7UaVfCuhOFbiaZ1xp3eTTXkApNWiSqNImnlysvDDlzbbMbeZnNWqZVIhGMgVrFCkmu16OLH4OVbykDOGHuOMXY+wT/3AgDn/EHOeQuAHwL4XLLX4Zw/zDnv5Zz32mw28a6AkAKxGdRQyWWYzOKG5+lxF/a1ZtYItJY11hTk8KzA7Q9iYcP42o2aq3UJd+QefxB9k4u4aZsVHVY9phf98b8c0jWx4IMnEKKKlRTaavSYmN+6ekgsKedocs7vSPO1/gPAfwH4Sk4rIqREyWQMjWZNxjvypUAIgzNu3Hlbd9bvvXp2ZwCeQLQaZetArk2YNnltZB7hCMeRbVbMe6M3T684vBkFZbrRmZ4Wiw6eQAguXzDv0yFzrVpZ+yfzXQAu5rYcQkpbU3Xmc8nPTboQ4UjraLdk4jvypcCWpYeCFosOkwubx+6+POyARinDgTYzOmLzXjLNk1+YWoRcxrC9zpjR8ypNIStXcs2R/20szXIOwNsAPCDCmggpWdnUkscnHmbYCLSW1bja3TmeYA75Rs3VWiwHw3B6189nOX7ZgYPtFqgV8nggzzRPfmHKje5aAzRKeUbPqzRCIB8rQCBP74iSJDjn7xFrIYRIQZNZhzlPAP5gOO1A1jfhQodVD7Mu+4/XNfrVHPnckh8mrRImbfLGorXTGoXdvN3tx9DsEt5zoBkAoFXJ0WjSZLEjd+Pmbms2l1FRWiyFmw1PnZ2EZECoJZ9e9Kf9nKFZD3Y15JaGUClkMOuUsR355mFZGyUKIq9cjnZzHtm2GoQ7bQaMZNDdaff4MecJ0I3ONOhUCtiM6oKMs6VATkgG4rXkaebJ/cEwxuZ96K7NPZ9sNagx54nmyFMF8tWxu6vrfGXYCbNOue58zQ6rHiMOb9qVFXSjMzOFmoJIgZyQDKRqf99o2L4EzoEd9WIEchXsHj8mFzbPId/IqFHCrFPG18k5xyvDDhzpsq4rgeyw6uHxhzbl0pPpjwXyHgrkaaFATkgJajRroVXKMTTrSevxgzPRx4lR4WE1qDEw7UEwzNFWs3UgB6JHjgk78isOL6YX/Ti8rWbdYzptmd3w7J9yo9Wiy2rwVyVqsegwtbiMlVB+x9lSICckA3IZw84GY3xnmsqQ3QOVXIb2NAJvKlaDOj4jJVVqBcC6AyZeGY7mx2/atv4mZWdsVkq6M1cuTC1SWiUDbRYdOM/9rNdUKJATkqGehir0T7vTyisPzXjQadMnHG6VKeGkICCTQL6MSITj5WEHmszaTc9rqtZCJZeltSP3+IMYdfookGegtaYwteQUyAnJUE9jFTz+UFqNQUOzS6I1zgjdnfIk42s3arHosBKKYNbjx4nLTty0zbrpNB+5jKGtRoeRNEoQB6ajaSKqWElfoZqCKJATkiGh6qN/euv0ylIghKuuZVFudAKrTUFN5sTjazcSbsz++vwM3P4QjiSp/e606dMqQbwgHLZMO/K02QxqqBUyjDuzmzKZLgrkhGRoZ30VZAwp8+SXZsW70Qmstumnk1YBVpuCHjs5AQA43FWT8HEdVgPG530IpThf8sKUG1aDGrVVdNhyumQyhpYCVK5QICckQ1pVtL091Y58KB7IxTl8QQjkqUoPBcKO/OKMBzvrjfHnb9Rp0yMY5ilTRRdodG1W2iw6jKc4DDtXFMgJyUJPoynljnxwZgkapQwt1blXrADRQF6jV2Fvc3o5ap1KgZrY1L2N1SprdaYxPMvtD+LSrAd7mig/nqkWiy7v42wpkBOShZ6GKlx1LWNxiwOOL9k96K41Zj2DfCOVQobjX74N7+9tSfs5wq78yBaBPD48a4tAfmxwDqEIx6076SyBTLVadFgKhOJjg/OBAjkhWRA6G7dKrwzOeEQf9apWyDP6i6HZooNCxnCow5L0MRa9Ciatcssbns/2z6JGr8K+LA+PrmSFqFyhQE5IFlJVrrh8K7B7AthRX9zDiT91pAN/9e5roFcnH3TKGEOHNfn5ncFwBL8ZtOO2nbV0RmcWClFLntMYW0Iqlc2ohs2oTponH5qN7m67i3z4wnVt1biuLfUuutOmx/FhZ8LvnbwyD48/hDt66sReXkUQ7pHkc5wt7cgJyZLQ4ZnIYKxiZYdETtHptOox4/bDG9h8fuezA7NQK2Q0gzxLWpUctUZ1Xg9ipkBOSJZ6GqswbPckHIh0adYDo1qRVgdmKei0CTNX1qdXOOd4bmAWN22zQqeiD/DZyvcURArkhGSpp6EKwTDHJfvmSYiDMx501xk2tcSXqmTndw7NLmFifpnSKjlqjZUg5gsFckKyFK9c2ZAn55xjaNYjWmt+IbTXJA7kz/bPAABu31lb8DWVk9YaHabdfgRC4by8PgVyQrLUXqOHVinflCd3LK1gwRcU5VSgQtGq5GgyazeVID47YMfeFjO15eeoNTbONp1Ba9mgQE5IlpLNJhdmrEhpRw5gUwmi3e1H34QLd+6i3Xiu8l1LToGckBwkmk0uVKx0izRjpVCiUxBXz+98/qIdACg/LgIhkOcrT06BnJAcJJpNPjTrQbVOGZ8fLhUdVj08gRAcS9FW8uf6Z9Fi0UqmhLKU2YxqaJQyjOepBJECOSE5SNThOTS7hO46o2QqVgRCCeLI3BJ8KyG8POzAHbvqJHcdpYgxltcSRArkhORg42xyzjmGZjyS3MWunYL40iUHAqEI7txFaRWx5DOQU4U/ITnYOJt8xu2HJxDCdond6ASARrMWKoUMIw4vFsYWYNQocHCLYVskMy0WHY5fdoJzLvqnHNqRE5KjtbPJB2dih0nUSutGJxCtwmmv0WHYvoQXLtpx645aKEU4NJpEtVp08K2E4czDOFv6XSIkR2tnkw+JfLxboXVY9Xj5kgNO7wpVq4gsnyWIFMgJydHa2eRDs0uwGdWojp3MIzWdNgNWwhEoZAy3bKdDJMTUaTPgYHs18nFQEOXICcnR2sqVoVlp3ugUCDNXbuisgUmrLPJqykuHVY8ff/ZwXl6bduSE5EiYTX7h6iIuzS5JNq0CAF2xEsTbqZtTUkQJ5IyxLzDGOGOMBhaTitTTUIUXBu1YDoaxXWIdnWsdaDXjG+/biw8dai32UkgGcg7kjLEWAHcCGM99OYRIU09jFVyxg5ilWHooYIzhvdc1Q6OUF3spJANi7Mi/CeCLAPKQwidEGoQ8OQB0S7D0kEhbToGcMfYuAFc5531pPPZ+xtgpxtipubm5XN6WkJIjVK40mbUwaugmISmslFUrjLHnANQn+NaDAP4UwNvSeSPO+cMAHgaA3t5e2r2TsiLMJpdyfpxIV8pAzjm/I9HXGWN7AHQA6Iu1mzYDOM0YO8Q5nxF1lYSUOLmM4c/v6UG7VVfspZAKlHUdOef8TQDxGiXG2CiAXs65Q4R1ESI5H76eKj1IcVAdOSGESJxonZ2c83axXosQQkj6aEdOCCESR4GcEEIkjgI5IYRIHAVyQgiROArkhBAicRTICSFE4hjPx3EVqd6UsTkAY1k+3QqgEpuO6LorT6VeO113cm2c801HNxUlkOeCMXaKc95b7HUUGl135anUa6frzhylVgghROIokBNCiMRJMZA/XOwFFAldd+Wp1Gun686Q5HLkhBBC1pPijpwQQsgaFMgJIUTiJBXIGWN3M8YGGWPDjLEvFXs9+cIY+3fGmJ0xdn7N1yyMsWcZY5di/64u5hrzgTHWwhj7DWNsgDF2gTH2QOzrZX3tjDENY+x1xlhf7Lr/Mvb1sr5uAWNMzhg7wxh7Kvbrsr9uxtgoY+xNxthZxtip2Neyvm7JBHLGmBzAtwG8HUAPgA8xxnqKu6q8+S6Auzd87UsAnuecdwN4PvbrchMC8Eec810AbgDw+7Hf43K/9gCA2zjnewHsA3A3Y+wGlP91Cx4AMLDm15Vy3bdyzvetqR3P+rolE8gBHAIwzDkf4ZyvAHgUwL1FXlNecM5fBDC/4cv3Avhe7L+/B+DdhVxTIXDOpznnp2P/7UH0h7sJZX7tPGop9ktl7B+OMr9uAGCMNQN4J4B/XfPlsr/uJLK+bikF8iYAE2t+PRn7WqWo45xPA9GAhzXnpZYjxlg7gP0AXkMFXHssvXAWgB3As5zzirhuAP8DwBcBRNZ8rRKumwN4hjH2BmPs/tjXsr5u0Y56KwCW4GtUO1mGGGMGAD8F8HnOuZuxRL/15YVzHgawjzFmBvAEY+yaIi8p7xhj9wCwc87fYIy9tcjLKbQjnPMpxlgtgGcZYxdzeTEp7cgnAbSs+XUzgKkiraUYZhljDQAQ+7e9yOvJC8aYEtEg/kPO+c9iX66IawcAzrkLwG8RvUdS7td9BMC7GGOjiKZKb2OM/QDlf93gnE/F/m0H8ASiqeOsr1tKgfwkgG7GWAdjTAXggwCeLPKaCulJAB+P/ffHAfy8iGvJCxbdev8bgAHO+f+/5ltlfe2MMVtsJw7GmBbAHQAuosyvm3P+Zc55c+zg9g8CeIFz/lGU+XUzxvSMMaPw3wDeBuA8crhuSXV2MsbegWhOTQ7g3znnXy/uivKDMfYjAG9FdKzlLICvAPhPAI8DaAUwDuB9nPONN0QljTF2E4CXALyJ1ZzpnyKaJy/ba2eMXYvozS05opurxznnX2OM1aCMr3utWGrlC5zze8r9uhljnYjuwoFoevs/OOdfz+W6JRXICSGEbCal1AohhJAEKJATQojEUSAnhBCJo0BOCCESR4GcEEIkjgI5IYRIHAVyQgiRuP8DzX7Mx58wDSQAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.plot(np.random.randn(50).cumsum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
