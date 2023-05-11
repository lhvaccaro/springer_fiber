%make x

word = "bmtbmbmtt";
word2 = "bmtbmt";
letters_used = ['b', 'm', 't'];

%word = word2;
% generating the matrix x from the word

% initializing variables we will need for the function. 
word_length = strlength(word);
block_size = size(letters_used);

% first, make an nxn square matrix of 0's, where n = length of the word.
x_matrix = zeros(word_length, word_length);


% now, we fill in the 1's as needed on a diagonal line
for i = 1:(word_length-1)
    x_matrix(i,i+1) = 1;
    if (mod(i,block_size) == 0)
        x_matrix(i,i+1) = 0;
    end
end

disp(x_matrix);

%fprintf(x_matrix)
sympref('MatrixWithSquareBrackets', true)
sym(x_matrix);

% matrix multiplication notes:
% M1*M1
% M1.*M2 for element by element multiplication

