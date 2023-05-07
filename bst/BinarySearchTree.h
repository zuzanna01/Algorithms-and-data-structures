#pragma once
#include <cassert>
#include <memory>
#include <string>
#include <ostream>
#include <iomanip>

template<typename KeyType, typename ValueType>
class Node {
public:
	KeyType* key;
	ValueType value;
	Node* left, * right;

	Node(KeyType key, ValueType value);
	std::string to_string() const;
	~Node();
};

template<typename KeyType, typename ValueType>
class BinarySearchTree
{
public:
	Node <KeyType, ValueType>* root = NULL;
	size_t numberOfNodes = 0;
	BinarySearchTree();

	size_t size() const;

	void insert(KeyType const& key, ValueType const& value);

	void remove(KeyType const& key);

	ValueType* find(KeyType const& key);

	std::string toString() const;

	template<typename StreamType>
	void print(StreamType& stream) const;

	Node <KeyType, ValueType>* findTheClosest(Node <KeyType, ValueType>* node, KeyType const& key);
	~BinarySearchTree();

};

template<typename KeyType, typename ValueType>
std::ostream& operator <<(std::ostream& stream, BinarySearchTree<KeyType, ValueType> const& tree)
{
	tree.print<std::ostream>(stream);
	return stream;
}
