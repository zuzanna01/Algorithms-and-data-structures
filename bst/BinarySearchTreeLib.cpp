#include <iostream>
#include "..\BinarySearchTreeLib\BinarySearchTree.h"

//----------Node class-----------------
template<typename KeyType, typename ValueType>
Node<typename KeyType, typename ValueType>::Node(KeyType key, ValueType value) {
	this->key = new KeyType(key);
	this->value = value;
	left = right = nullptr;
}
template<typename KeyType, typename ValueType>
std::string Node<KeyType, ValueType>::to_string() const
{
	std::string node_str = "[" + this->key + ", " + this->value + "]";
	return node_str;
}
template<typename KeyType, typename ValueType>
Node<KeyType, ValueType>::~Node()
{
	delete right;
	delete left;
	delete key;
	delete value;
};
//-------------BST class--------------------------
template<typename KeyType, typename ValueType>
BinarySearchTree<KeyType, ValueType>::BinarySearchTree() {
	this -> root = nullptr;
	this -> numberOfNodes = 0;
}

template<typename KeyType, typename ValueType>
BinarySearchTree<KeyType, ValueType>::~BinarySearchTree()
{
}

template<typename KeyType, typename ValueType>
size_t BinarySearchTree<typename KeyType, typename ValueType>::size() const {
	return this->numberOfNodes;
};

template<typename KeyType, typename ValueType>
Node<KeyType, ValueType>* BinarySearchTree<KeyType, ValueType>::findTheClosest(Node<KeyType, ValueType>* node, KeyType const& key)
{

	Node< KeyType, ValueType>* prev = nullptr;
	Node< KeyType, ValueType>* temp = node;

	while (temp) {
		if (*(temp->key) > key) {
			prev = temp;
			temp = temp->left;
		}
		else if (*(temp->key) < key) {
			prev = temp;
			temp = temp->right;
		}
		else if (*(temp->key) == key) {
			break;
		}
	}
	return prev;
}

//---------------INSERT---------------
template<typename KeyType, typename ValueType>
void BinarySearchTree<typename KeyType, typename ValueType>::insert(KeyType const& key, ValueType const& value) {

	Node< KeyType, ValueType>* node = new Node< KeyType, ValueType>(key, value);

	if (this->root == nullptr || *(this -> root -> key) == key) {
		this->root = node;
		this->numberOfNodes++;
	}
	else {
		Node< KeyType, ValueType>* closest = findTheClosest(this->root, key);

		if (*(closest->key) > key && closest->left == nullptr) {
			closest->left = node;
			this->numberOfNodes++;
		}
		if (*(closest->key) < key && closest->right == nullptr) {
			closest->right = node;
			this->numberOfNodes++;
		}

	}

}

//--------------FIND-------------------
template<typename KeyType, typename ValueType>
ValueType* BinarySearchTree<typename KeyType, typename ValueType>::find(KeyType const& key) {
	if (this->root == nullptr) {
		return nullptr;
	}
	else if (*(this->root->key) == key) {
		return &(this->root->value);
	}
	else {
		Node< KeyType, ValueType>* closest = findTheClosest(this->root, key);
		if (closest->right != nullptr && *(closest->right ->key) == key) {
			return &(closest->right->value);
		}
		if (closest->left != nullptr && *(closest->left->key) == key) {
			return &(closest->left->value);
		}

		return nullptr;
	}
}

//----------------REMOVE----------------------------
template<typename KeyType, typename ValueType>
void BinarySearchTree<typename KeyType, typename ValueType>::remove(KeyType const& key) {

	if (this->root == NULL) {
		return;
	}
	else {

		Node< KeyType, ValueType>* prev = findTheClosest(this->root, key);
		Node< KeyType, ValueType>* temp;
		
		if (prev == nullptr && *(this->root->key) == key) {
			temp = this->root;
		}
		else if (prev->left == nullptr || prev->right == nullptr) {
			return;
		}
		else if (*(prev->left->key) == key) {
			temp = prev->left;
		}
		else if (*(prev->right->key) == key) {
			temp = prev->right;
		}
		else return;
		

		// node without children
		if (temp->left == nullptr && temp->right == nullptr) {
			
			if (temp == this->root) this->root = NULL;
			if (prev != NULL && prev->right == temp)prev->right = NULL;
			if (prev != NULL && prev->left == temp)prev->left = NULL;

		}
		
		// node with one right children
		if (temp->left == NULL && temp->right != NULL) {

			//root
			if (temp == this->root) {
				this->root = temp->right;
				numberOfNodes--;
				return;
			}

			// right child
			if (prev->right == temp) {
				prev->right = temp->right;
			}
			
			// left child
			if (prev->left == temp) {	
				prev->left = temp->right;
			}


		}
			
		//node with one left children
		if (temp->left != NULL && temp->right == NULL) {

			//root
			if (temp == this->root) {
				this->root = temp->left;
				numberOfNodes--;
				return;
			}

			//right child
			if (prev->right == temp) {
				prev->right = temp->left;
			}

			//left child
			if (prev->left == temp) {
				prev->left = temp->left;
			}

		}
			
		// node with two children // inorder predecessor
		if (temp->left != NULL && temp->right != NULL) {

		
			Node< KeyType, ValueType>* preSuccessor = findPreSuccessor(temp->left, *(temp->key));
			Node< KeyType, ValueType>* successor = preSuccessor->right;
			//successor doesn't have kid
			if (successor->left == nullptr) {
				preSuccessor->right = nullptr;
				successor->left = temp->left;
				successor->right = temp->right;
				if(prev->left==temp)prev->left=successor;
				else prev->right = successor;
			}
			else {
				preSuccessor->right = successor->left;
				successor->left = temp->left;
				successor->right = temp->right;
				if (prev->left == temp)prev->left = successor;
				else prev->right = successor;
			}

		}

		numberOfNodes--;
		return;
	}

		
};

template<typename KeyType, typename ValueType>
Node<KeyType, ValueType>* findPreSuccessor(Node<KeyType, ValueType>* node, KeyType const& key)
{
	Node< KeyType, ValueType>* preprev = nullptr;
	Node< KeyType, ValueType>* prev = nullptr;
	Node< KeyType, ValueType>* temp = node;

	while (temp) {
		if (*(temp->key) > key) {
			preprev = prev;
			prev = temp;
			temp = temp->left;
		}
		else if (*(temp->key) < key) {
			preprev = prev;
			prev = temp;
			temp = temp->right;
		}
		else if (*(temp->key) == key) {
			break;
		}
	}
	return preprev;
}



int depth;
template<typename KeyType, typename ValueType, typename StreamType>
int traversePreorder2(Node< KeyType, ValueType>* root, StreamType& stream, std::string letter = "")
{


	if (root == NULL) {
		return 0;
	}

	for (int i = depth; i > 0; i--) {
		stream << "    ";
	}
	stream << letter << "[" << *(root->key) << ", " << root->value << "]" << "\n";

	depth++;
	traversePreorder2(root->left, stream, "L: ");

	traversePreorder2(root->right, stream, "R: ");
	depth--;
	return 0;
}

template<typename KeyType, typename ValueType>
template<typename StreamType>
void BinarySearchTree<typename KeyType, typename ValueType> ::print(StreamType& stream) const {
	if (this->root == NULL) {
		stream << "";
	}
	else {
		depth = 0;
		traversePreorder2(this->root, stream);
	}
};

template<typename KeyType, typename ValueType>
std::string BinarySearchTree<KeyType, ValueType>::toString() const
{
	return traversePreorder1(this->root);
}



template<typename KeyType, typename ValueType>
std::string traversePreorder1(Node<KeyType, ValueType>* node) {
	if (node == NULL) { return ""; }
	std::stringstream str_tree("");
	str_tree << "([" << *(node->key) << "," << node->value << "]," << traversePreorder1(node->left) << "," << traversePreorder1(node->right) << ")";
	return str_tree.str();
}
