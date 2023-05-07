#pragma once
#include <cassert>
#include <memory>
#include <string>
#include <ostream>
#include <iomanip>
#include <sstream>

template<typename KeyType, typename ValueType>
class Node
{
public:
	KeyType* key;
	ValueType* value;
	Node* left = NULL;
	Node* right = NULL;
	Node* prev = NULL;
	int height = 1;

	Node(KeyType key, ValueType val);
	int get_ballance();
};

template<typename KeyType, typename ValueType>
class AVLTree
{
public:
	Node <KeyType, ValueType>* root = NULL;
	size_t size() const;
	int height(KeyType* N);

	void insert(KeyType const& key, ValueType const& value);
	void rotate_left(Node<KeyType, ValueType>* Q, Node<KeyType, ValueType>* P);
	void rotate_right(Node<KeyType, ValueType>* Q, Node<KeyType, ValueType>* P);

	ValueType* find(KeyType const& key);

	std::string toString() const;
	std::string printNode(Node<KeyType, ValueType>* N) const;

	template<typename StreamType>
	void print(StreamType& stream) const { stream << toString(); }
	size_t numberOfNodes = 0;

};

template<typename KeyType, typename ValueType>
std::ostream& operator <<(std::ostream& stream, AVLTree<KeyType, ValueType> const& tree)
{
	tree.print<std::ostream>(stream);
	return stream;
}
