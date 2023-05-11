%make x

word = 'bmtbmbmtt';
word2 = 'bmtbmt';
letters_used = ['b', 'm', 't'];

%word = word2;
% generating the matrix x from the word

% initializing variables we will need for the function. 
word_length = strlength(word);
block_size = word_length/length(letters_used);
%block_size = length(letters_used);


% first, make an nxn square matrix of 0's, where n = length of the word.
new_matrix = zeros(word_length, word_length);


% now, we fill in the 1's as needed on a diagonal line
b_counter =0;
m_counter =0;
t_counter =0;
prev_b= 0;
prev_m= 0;

M = cell(block_size,1);

%B = cell(1,block_size);
for i = 1:(word_length)
    if word(i) == 'b'

        b_counter = b_counter+1;
        new_matrix((b_counter+(2*block_size)),i)=1;

        prev_b = i;
    elseif word(i)== 'm'
        
        m_counter= m_counter+1;
        j=m_counter+block_size;

        new_matrix(j,i)=1;
        new_matrix(t_counter+1, i)= M{m_counter};
        for k=(t_counter+2):(block_size)
            new_matrix(k,i) = new_matrix(k-1, prev_m);

        end
        prev_m =i;
    elseif word(i)=='t'


        t_counter= t_counter+1;
        new_matrix(t_counter,i)=1;
    end

    %disp(b_counter)
end

disp(new_matrix);

%image(x_matrix);

% matrix multiplication notes:
% M1*M1
% M1.*M2 for element by element multiplication