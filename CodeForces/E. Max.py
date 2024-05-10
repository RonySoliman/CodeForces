{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59edf598",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n",
      " 1 2 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "num:  3\n"
     ]
    }
   ],
   "source": [
    "# E. Max\n",
    "# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/E\n",
    "\n",
    "values = int(input())\n",
    "checker = list(map(int, input().split()))\n",
    "\n",
    "for values in range(1,1000):\n",
    "    for i,j in enumerate(checker):\n",
    "        num = max(checker)\n",
    "    print(num)\n",
    "    break\n",
    "    \n",
    "# https://stackoverflow.com/questions/29811082/how-to-print-out-a-numbered-list-in-python-3"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
