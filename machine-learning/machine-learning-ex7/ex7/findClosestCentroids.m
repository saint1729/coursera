function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);

% You need to return the following variables correctly.
idx = zeros(size(X,1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
%

dist = zeros(size(X,1), K);


for i = 1:K
  %d = zeros(size(X,1),1);
  %for j = 1:size(X,1)
	  %c = bsxfun(@minus, X(:,j), centroids(i,j));
	  %d = bsxfun(@power, c, 2);
	  %c2 = bsxfun(@minus, X(:,2), centroids(i,2));
	  %d2 = bsxfun(@power, c2, 2);
    %dist(j,:) = d;
  %endfor
  %for j = 1:m
  %  c = bsxfun(@minus, X(j,:), centroids(i,:));
	%  d = bsxfun(@power, c, 2);
	%  dist(:,i) = sum(d.^2);
  c = bsxfun(@minus, X, centroids(i,:));
  dist(:,i) = sum(c.^2, 2);
endfor


%for i = 1:m
[min_values indices] = min(dist');
idx = indices;
idx = idx(:);
% =============================================================

%a = idx(1,1)
%a = idx(2,1)
%a = idx(3,1)
%a = idx(4,1)
%a = idx(5,1)

end

