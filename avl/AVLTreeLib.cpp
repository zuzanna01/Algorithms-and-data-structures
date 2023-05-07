#include "AVLTree.h"

int max(int a, int b)
{
	return (a > b) ? a : b;
}

template<typename KeyType, typename ValueType>
void calc_height(Node<typename KeyType, typename ValueType>* A) {
	if (A != NULL) {
		if (A->left != NULL && A->right != NULL) {
			A->height = max(A->left->height, A->right->height) + 1;
		}
		if (A->left != NULL && A->right == NULL) {
			A->height = A->left->height + 1;
		}
		if (A->left == NULL && A->right != NULL) {
			A->height = A->right->height + 1;
		}
		if (A->left == NULL && A->right == NULL) {
			A->height = 1;
		}
	}
}
// Node constructor

template<typename KeyType, typename ValueType>
Node<typename KeyType, typename ValueType>::Node(KeyType key, ValueType value) {
	this->key = new KeyType(key);
	this->value = new ValueType(value);
}

template<typename KeyType, typename ValueType>
int Node<typename KeyType, typename ValueType>::get_ballance() {
	if (this != NULL) {
		if (this->left != NULL && this->right != NULL) {
			return this->left->height - this->right->height;
		}
		if (this->left != NULL && this->right == NULL) {
			return this->left->height;
		}
		if (this->left == NULL && this->right != NULL) {
			return -this->right->height;
		}
		if (this->left == NULL && this->right == NULL) {
			return 0;
		}
	}
	return 0;
}


// AVLTree class methods

template<typename KeyType, typename ValueType>
size_t AVLTree<typename KeyType, typename ValueType>::size() const {
	return this->numberOfNodes;
}

template<typename KeyType, typename ValueType>
int AVLTree<typename KeyType, typename ValueType>::height(KeyType* N) {
	if (N == NULL)
		return 0;
	return N->height;
};

template<typename KeyType, typename ValueType>
void AVLTree<typename KeyType, typename ValueType>::insert(KeyType const& key, ValueType const& value) {

	Node< KeyType, ValueType>* node = new Node< KeyType, ValueType>(key, value);

	if (this->root == NULL) {
		this->root = node;
		this->numberOfNodes += 1;
	}
	else {
		Node< KeyType, ValueType>* temp = this->root;
		Node< KeyType, ValueType>* prev = NULL;
		while (temp) {
			if (*(temp->key) == key) {
				*(temp->value) = value;
				return;
			}
			else if (*(temp->key) > key) {
				prev = temp;
				temp = temp->left;
			}
			else if (*(temp->key) < key) {
				prev = temp;
				temp = temp->right;
			}
		}
		if (*(prev->key) > key) {
			prev->left = node;
			node->prev = prev;
			this->numberOfNodes++;
			temp = node;
		}
		else {
			prev->right = node;
			node->prev = prev;
			this->numberOfNodes++;
			temp = node;
		}
		while (temp != NULL) {
			if (temp->get_ballance() > 1) {
				if (temp->left->get_ballance() == 1) {
					rotate_right(temp, temp->left);
				}
				else {
					rotate_left(temp->left, temp->left->right);
					rotate_right(temp, temp->left);
				}
			}
			else if (temp->get_ballance() < -1) {
				if (temp->right->get_ballance() == -1) {
					rotate_left(temp->right, temp);
				}
				else {
					rotate_right(temp->right->left, temp->right);
					rotate_left(temp->right, temp);
				}
			}
			
			temp = temp->prev;
			calc_height(temp);
		}
	}
}

template<typename KeyType, typename ValueType>
void AVLTree<typename KeyType, typename ValueType>::rotate_left(Node<KeyType, ValueType>* Q, Node<KeyType, ValueType>* P) {
	if (P == this->root) { 
		this->root = Q;
		Q->prev = NULL;
	}
	else {
		if (P->prev->left == P) { P->prev->left = Q; }
		if (P->prev->right == P) { P->prev->right = Q; }
		Q->prev = P->prev;
	}
	if (P->right != NULL && Q->left != NULL) {
		P->right = Q->left;
		P->right->prev = P;
	}
	else { P->right = NULL; }
	Q->left = P;
	P->prev = Q;
	
	calc_height(P);
	calc_height(Q);
}

template<typename KeyType, typename ValueType>
void AVLTree<typename KeyType, typename ValueType>::rotate_right(Node<KeyType, ValueType>* Q, Node<KeyType, ValueType>* P) {
	if (Q == this->root) { 
		this->root = P;
		P->prev = NULL;
	}
	else {
		if (Q->prev->left == Q) { Q->prev->left = P; }
		if (Q->prev->right == Q) { Q->prev->right = P; }
		P->prev = Q->prev;
	}
	if (Q->left != NULL && P->right != NULL) {
		Q->left = P->right;
		Q->left->prev = Q;
	}
	else { Q->left = NULL; }
	P->right = Q;
	Q->prev = P;
	calc_height(P);
	calc_height(Q);
}

template<typename KeyType, typename ValueType>
ValueType* AVLTree<typename KeyType, typename ValueType>::find(KeyType const& key) {
	Node< KeyType, ValueType>* temp = this->root;
	while (temp != NULL) {
		if (key == *(temp->key)) {
			return temp->value;
		}
		else if (key > *(temp->key)) {
			temp = temp->right;
		}
		else if (key < *(temp->key)) {
			temp = temp->left;
		}	
	}
	return NULL;
}

template<typename KeyType, typename ValueType>
std::string AVLTree<KeyType, ValueType>::toString() const
{
	return printNode(this->root);
}
template<typename KeyType, typename ValueType>
std::string AVLTree<KeyType, ValueType>::printNode(Node<KeyType, ValueType>* N) const {
	if (N == NULL) { return ""; }
	std::stringstream result;
	result << "([" << *(N->key) << "," << *(N->value) << "]," << printNode(N->left) << "," << printNode(N->right) << ")";
	return result.str();
}
