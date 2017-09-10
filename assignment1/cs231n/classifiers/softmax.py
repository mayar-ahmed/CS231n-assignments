import numpy as np
from random import shuffle
from past.builtins import xrange


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    num_training = X.shape[0]
    num_classes = W.shape[1]
    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    for i in xrange(num_training):
        f = X[i].dot(W)
        f -= np.max(f)
        p = np.exp(f) / np.sum(np.exp(f))
        loss += -1 * np.log(p[y[i]])
        for j in xrange(num_classes):
            if j == y[i]:
                dW[:, j] += (p[j] - 1) * X[i]
            else:
                dW[:, j] += p[j] * X[i]

    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    loss /= num_training
    dW /= num_training

    loss += reg * np.sum(W * W)
    dW += 2 * reg * W

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    num_training = X.shape[0]
    num_classes = W.shape[1]

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    scores = X.dot(W)
    scores -= np.max(scores, axis=1).reshape((-1, 1))
    p = np.exp(scores) / (np.sum(np.exp(scores), axis=1).reshape((-1, 1)))
    loss = np.sum(-1 * np.log(p[np.arange(p.shape[0]), y]))
    loss /= num_training
    loss += reg * np.sum(W * W)

    ####gradient####
    t = p
    t[np.arange(t.shape[0]), y] -= 1;
    dW = np.dot(X.T, t)
    dW /= num_training
    dW += 2 * reg * W

    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW
