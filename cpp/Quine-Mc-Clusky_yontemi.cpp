#include<iostream>
#include<vector>
using namespace std;
unsigned short int BIT_SIZE = 0;
typedef vector<int> Bit;
typedef vector<int> Index;
Index TERIMLER;
 struct Term {
	 Term() {}
	 Term(int x)
	 {
		 for (size_t i = 0; i < BIT_SIZE; i++)
		 {
			this->bits.push_back((x>>i) & 1);
		 }
		 this->index.push_back(x);
	 }
	Bit bits;
	Index index;
};
 bool isHasTerm(vector<Term>liste, Term terim);
 vector<int> setIndex(Index index1, Index index2);
 bool compareTerm(Term terim1, Term terim2, Term &result);
 int maxBit(vector<int>dizi);
 vector<Term> resultList(vector<Term>liste);
 vector<Term> baslangic();
 bool isAsal(Term terim, vector<Term>liste, int jump);
 void resultAsal(vector<Term>liste);
 vector<Term> RemoveIndex(Index x, vector<Term> liste);
void main()
{
	vector<Term> terimler = baslangic();
	terimler=resultList(terimler);
	cout << endl;
	resultAsal(terimler);
 	exit(EXIT_SUCCESS);
}

bool isAsal(Term terim, vector<Term>liste, int jump)
{
	int c;
	for (size_t i = 0; i < terim.index.size(); i++)
	{
		c = 0;
		for (size_t j = 0; j < liste.size(); j++)
		{
			if (j != jump)
			{
				for (size_t k = 0; k < liste[j].index.size(); k++)
				{
					if (liste[j].index[k] == terim.index[i])
					{	if(liste[j].index.size()!=1)
						c++;
					}
				}
			}
		}
		if (c == 0)
		{
			return true;
		}
	}
	return false;
}
vector<Term> RemoveIndex(Index x,vector<Term> liste)
{
	Index temp;
	for (size_t k = 0; k < x.size(); k++)
	{
		for (size_t i = 0; i < liste.size(); i++)
		{
			for (size_t j = 0; j < liste[i].index.size(); j++)
			{
				if (x[k] != liste[i].index[j])
				{
					temp.push_back(liste[i].index[j]);
				}
			}
			liste[i].index = temp;
			temp.clear();
		}
	}
	
	return liste;
}
void resultAsal(vector<Term>liste)
{
	char Harf ;
	bool kontrol;
	size_t len;
	bas:
	for (size_t i = 0; i < liste.size(); i++)
	{
		if (isAsal(liste[i], liste, i))
		{
			liste = RemoveIndex(liste[i].index, liste);
			Harf = 'A';
			len = liste[i].bits.size();
			for (size_t j =0; j<len ;j++)
			{
				int w = liste[i].bits.back();
				liste[i].bits.pop_back();
				switch (w)
				{
				case 1:
					cout << Harf;
					Harf++;
					break;
				case 0:
					cout << Harf << "'";
					Harf++;
					break;
				default:
					Harf++;
					break;
				}
			}
			kontrol = false;
			for (size_t q = 0; q < liste.size(); q++)
			{
				if (liste[q].index.size() != 0)
					kontrol = true;
			}
			if(kontrol)
			  cout << " + ";
			goto bas;
		}
	}
}

int maxBit(vector<int>dizi)
{
	int max = 0;
	for (size_t i = 0; i < dizi.size(); i++)
	{
		if (dizi[i] > max)
			max = dizi[i];
	}
	for (int j = 0; j < 64; j++)
		if ((int)pow(2, j)>max)
			return j;
	return 0;
}

vector<Term> baslangic()
{

	int x = 0, sayac = 0;
	vector<Term>liste;
	cout << "MinTerim sayisi..:";
	cin >> sayac;
	cout << "MinTerimleri giriniz(orn; 1 2 3 11 13 15)..:";
	for (int i = 0; i < sayac; i++)
	{
		cin >> x;
		TERIMLER.push_back(x);
		
	}
	BIT_SIZE = maxBit(TERIMLER);
	for (int i = 0; i < sayac; i++)
	{
		liste.push_back(Term(TERIMLER[i]));
	}
	return liste;
}
vector<Term> resultList(vector<Term>liste)
{
	bool complete = false;
	vector<Term> temp = liste;
	while (!complete)
	{
		complete = true;

		vector<Term>*yeniliste = new vector<Term>;
		for (size_t i = 0; i < temp.size(); i++)
		{
			bool isCompare = false;
			for (size_t j = 0; j < temp.size(); j++)
			{
				Term *result = new Term;
				if (compareTerm(temp[i], temp[j], *result))
				{
					if (!isHasTerm(*yeniliste, *result))
					{
						(*yeniliste).push_back(*result);

					}
					isCompare = true;
					delete result;
				}
			}
			if (isCompare == false)
			{
				if (!isHasTerm(*yeniliste, temp[i]))
				{
					(*yeniliste).push_back(temp[i]);
				}
			}


		}


		for (size_t i = 0; i < yeniliste->size(); i++)
		{
			if (!isHasTerm(temp, (*yeniliste)[i]))
			{
				complete = false;
			}
		}
		temp = *yeniliste;
		delete yeniliste;
	}
	return temp;
}
bool compareTerm(Term terim1, Term terim2, Term &result)
{
	int t = 0;
	for (size_t i = 0; i < BIT_SIZE; i++)
	{
		if (terim1.bits[i] != terim2.bits[i])
		{
			result.bits.push_back(2);
			t++;
			result.index = setIndex(terim1.index, terim2.index);
			continue;
		}
		result.bits.push_back(terim1.bits[i]);
	}
	return t == 1 ? 1 : 0;;

}
vector<int> setIndex(Index index1, Index index2)
{
	vector< int>temp;
	int len1 = index1.size();
	int len2 = index2.size();
	int x = 0;
	bool isHas = false;
	for (int i = 0; i < len1; i++)
	{
		int len3 = temp.size();
		x = index1.back();
		index1.pop_back();
		for (int j = 0; j < len3; j++)
		{
			if (temp[j] == x)
			{
				isHas = true;
				break;
			}
		}
		if (!isHas)
		{
			temp.push_back(x);
		}

	}
	x = 0;
	isHas = false;
	for (int i = 0; i < len2; i++)
	{
		int len3 = temp.size();
		x = index2.back();
		index2.pop_back();
		for (int j = 0; j < len3; j++)
		{
			if (temp[j] == x)
			{
				isHas = true;
				break;
			}
		}
		if (!isHas)
		{
			temp.push_back(x);
		}

	}
	return temp;
}
bool isHasTerm(vector<Term>liste, Term terim)
{
	int ishas = 0;
	size_t len = liste.size();
	size_t size = terim.bits.size();
	for (size_t i = 0; i < len; i++)
	{
		if (liste[i].bits.size() == terim.bits.size())
		{
			ishas = 0;
			for (size_t j = 0; j < size; j++)
			{
				ishas += liste[i].bits[j] == terim.bits[j] ? 1 : 0;
			}
			if (ishas == size)
			{
				return true;
			}

		}
	}
	return false;
}
