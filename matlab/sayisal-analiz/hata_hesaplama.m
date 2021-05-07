%HATALAR
%% DEGERLER
true_val = 1.1235614156;
predict_val=1.11;

%% BAGIL HATA - RELATIVE ERROR
relative_error = (true_val-predict_val) / true_val;
fprintf('Bagil Hata = %.4f \n',relative_error);

%% MUTLAK HATA - ABSOLUTE ERROR
absolute_error = abs(true_val-predict_val);
fprintf('Mutlak Hata = %.4f \n',absolute_error);

%% YÜZDE HATA - YÜZDE BAĞIL HATA
percentage_error = relative_error * 100;
fprintf('Mutlak Hata = %%%.4f \n',percentage_error);