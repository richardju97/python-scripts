#include<stdio.h>
#include<stdlib.h>

struct vertex
{
	int value;
	struct vertex *left;
	struct vertex *right;
};

struct vertex *tree = NULL;

struct vertex *create(int x);
void insert(int x);
void eliminate(int x);
void display(struct vertex *p);

int main()
{
	insert(3); insert(12); insert(18); insert(11); insert(14);
	eliminate(12); insert(2); insert(3);
	insert(6); eliminate(3); insert(5);
	eliminate(11); insert(7);eliminate(6);

	display(tree);
	return 0;
}

struct vertex *create(int x)
{
	struct vertex *p;
	p = (struct vertex *)malloc(sizeof(struct vertex));
	p->value = x;
	p->left = NULL;
	p->right = NULL;
	return p;
}

void insert(int x)
{
	struct vertex *p;

	if (tree == NULL)

		tree = create(x);
	return;



	p = tree;
	do
	{
		if (p->value == x)break;
		else if (x < p->value && p->left == NULL)
		{
			p->left = create(x);
			break;
		}
		else if (p->value < x&&p->right == NULL)
		{
			p->right = create(x);
			break;
		}
		if (x < p->value)
			p = p->left;
		else
			p = p->right;
	} while (1);
	return;
}

void eliminate(int x)
{
	struct vertex *f, *p, *q;
	p = tree;
	if (p == NULL) return;
	do
	{
		f = p;
		if (x < p->value)
			p = p->left;
		else if (p->value < x)
			p = p->right;
	  // 问题4答案	if (p == NULL) break;													//当输入一个里面没有的数删除时会有问题
	} while (x != p->value);

	if (p->left == NULL || p->right == NULL)
	{
		if (p->right == NULL)

			q = p->left;
		else
			q = p->right;
		if (p == tree)
			tree = q;
		else
		{
			if (f->left == p)
				f->left = q;
			else
				f->right = q;
		}
		// 85行到86行 free(p);
	}
	else
	{
		q = p->right;
		f = q;
		while (q->left != NULL)
		{
			f = q;
			q = q->left;
		}
		p->value = q->value;
		if (q == f)
			p->right = q->right;
		else
			f->left = q->right;
		//98行到99行，free（q);
	}
	return;
}

void display(struct vertex *p)
{
	if (p == NULL)return;
	printf("%d,", p->value);
	display(p->left);
	display(p->right);
	return;
}
	//问题7答案
	//display(p->right);
	//printf("%d,", p->value);
	//display(p->left);

	//问题8答案 
