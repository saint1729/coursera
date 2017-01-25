function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%

%for i = 1:m
%	J = J+(-1*y(i)*log(h(X(i)))-(1-y(i))*log(1-h(X(i))));
%endfor

h = sigmoid(X*theta);
%a = X;
t1 = y.*log(h);
o1 = ones(size(y));
o2 = ones(size(y));
%fprintf('\n%d %d\n', size(o1), size(o2));
t2 = (o1-y).*log(o2-h);
s = sum(t1)+sum(t2);

J = -1*s/m;

%for j = 1:size(grad)+1
%	grad(j) = 1/m*((h-y));
%endfor

theta(1) = 0;

grad = X'*(h-y);

grad = 1/m*grad;

% =============================================================

end
