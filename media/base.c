#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#define MAX 1000009

// IIT se hai BC  

int max(int a, int b){
	return a > b ? a : b;
}

typedef struct tri{
	int val;
	int size, height;
	struct tri *right, *left;
} tri;
int size(tri *root){
	return root ? root->size : 0;
}
int height(tri *root){
	return root ? root->height : 0;
}
int getBal(tri *root){
	if (root)
	return height(root->left) - height(root->right);
	return 0;
}
tri *lrt(tri *root){
	tri *y = root->right;
	tri *T2 = y->left;
	y->left = root;
	root->right = T2;
	root->height = max(height(root->left)+1, height(root->right)+1);
	y->height = max(height(y->left)+1, height(y->right)+1);
	root->size = 1 + size(root->left) + size(root->right);
	y->size = 1 + size(y->left) + size(y->right);
	return y;
}

tri *rrt(tri *root){
	tri *x = root->left;
	tri *T2 = x->right;
	x->right = root;
	root->left = T2;
	root->height = max(height(root->left), height(root->right)) + 1;
	x->height = max(height(x->left), height(x->right)) + 1;
	root->size = 1 + size(root->left) + size(root->right);
	x->size = 1 + size(x->left) + size(x->right);
	return x;
}

tri *insert(int val, int pos, tri *root){
	if (!root){
		tri *nwTri = (tri*) malloc(sizeof(tri));
		nwTri->val = val;
		nwTri->right = nwTri->left = NULL;
		nwTri->size = 1;
		nwTri->height = 1;
		return nwTri;		
	}
	int root_pos = size(root->left);
	if (root_pos >= pos)
		root->left = insert(val, pos, root->left);
	else
		root->right = insert(val, pos - root_pos - 1, root->right);
	root->size = 1 + size(root->left) + size(root->right);
	root->height = 1 + max(height(root->right), height(root->left));
	int bal = getBal(root);
	if (bal > 1){
		if (getBal(root->left) <= -1)
			root->left = lrt(root->left);
		root = rrt(root);
	}
	else if (bal < -1){
		if (getBal(root->right) >= 1)
			root->right = rrt(root->right);
	root = lrt(root);
	}
	return root;
}
tri *leftmostOf(tri *node){
	tri *there = node;
	while (there->left != NULL)
		there = there->left;
	return there;
}
tri *delN(int pos, tri *root){
	if (root == NULL)
		return root;
	int root_pos = (root->left ? root->left->size : 0);
	if (root_pos > pos)
		root->left = delN(pos, root->left);
	else if (root_pos < pos)
		root->right = delN(pos - root_pos - 1, root->right);
	else{
		if ((root->left == NULL) || (root->right == NULL)){
			tri *temp = root->left ? root->left : root->right;
				if (temp == NULL){
					temp = root;
					root = NULL;
				}
				else
					*root = *temp;
			}
		else{
			tri *leftmost = leftmostOf(root->right);
			root->val = leftmost->val;
			root->right = delN(0, root->right);
		}
	}
	if (root == NULL)
		return root;
	root->size = 1 + size(root->left) + size(root->right);
	root->height = 1 + max(height(root->right), height(root->left));
	int bal = getBal(root); // height(left) - height(right)
	if (bal > 1){
		if (getBal(root->left) <= -1){
			root->left = lrt(root->left);
		}
		root = rrt(root);
	}
	else if (bal < -1){
		if (getBal(root->right) >= 1){
			root->right = rrt(root->right);
		}
		root = lrt(root);
	}
	return root;
}

// tri *(int ){
// 	tri *nwTri = (e*) malloc(sizeof(tri));
// 	= val;
// 	nwTri->right = nwTri->left = NULL;
// 	nwTri->size = -1;
// 	nwTri->ht = 1;
// 	return nwTri;
// }
int calc(int pos, tri *root){
	int root_pos = (root->left ? root->left->size : 0);
	if (root_pos == pos)
		return root->val;
	else if (root_pos > pos)
		calc(pos, root->left);
	else
		calc(pos - root_pos - 1, root->right);
	//return -1;
}
int main(){
	int n, q, value,k,cmd;
	tri* root=NULL;
	scanf("%d %d", &n, &q);
	for (int i = 0; i < n; i++){scanf("%d", &value); root = insert(value, i, root);}
	for (int Q = 0; Q < q; Q++){
	scanf("%d %d", &cmd, &k);
	if(cmd==1){
		scanf("%d", &value);
		root = insert(value, k - 1, root);
		n++;
	}
	else if (cmd==2){
		root = delN(k - 1, root);
		n--;
		}
	else
		printf("%d\n",calc(k - 1, root));
	}
}