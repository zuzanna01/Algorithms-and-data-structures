#include <iostream>
#include <random>
#include <chrono>
#include <thread>
#include "..\BinarySearchTreeLib\BinarySearchTree.h"
#include "..\BinarySearchTreeLib\BinarySearchTreeLib.cpp"

template<typename D = std::chrono::microseconds>
class Benchmark
{
public:
	Benchmark(bool printOnExit = false) : m_print(printOnExit)
	{
		start = std::chrono::high_resolution_clock::now();
	}
	typename D::rep elapsed() const
	{
		auto end = std::chrono::high_resolution_clock::now();
		auto result = std::chrono::duration_cast<D>(end - start);
		return result.count();
	}
	~Benchmark()
	{
		auto result = elapsed();
		if (m_print)
		{
			std::cerr << "Time: " << result << "\n";
		}
	}
private:
	std::chrono::high_resolution_clock::time_point start;
	bool m_print = true;
};

class Key
{
private:
	static unsigned long long cmpCount;
	unsigned long value = 0UL;
public:
	static void resetCounter()
	{
		cmpCount = 0ULL;
	}

	static unsigned long long getCmpCount()
	{
		return cmpCount;
	}

	Key() = default;

	Key(Key const&) = default;

	Key(unsigned long v) : value(v)
	{
	}

	unsigned long getKey() const
	{
		return value;
	}

	bool operator==(Key const& v) const
	{
		++cmpCount;
		return value == v.value;
	}

	bool operator!=(Key const& v) const
	{
		++cmpCount;
		return value != v.value;
	}

	bool operator<(Key const& v) const
	{
		++cmpCount;
		return value < v.value;
	}
	bool operator<=(Key const& v) const
	{
		++cmpCount;
		return value <= v.value;
	}
	bool operator>(Key const& v) const
	{
		++cmpCount;
		return value > v.value;
	}
	bool operator>=(Key const& v) const
	{
		++cmpCount;
		return value >= v.value;
	}
};

unsigned long long Key::cmpCount = 0ULL;

std::ostream& operator << (std::ostream& stream, Key const& key)
{
	stream << key.getKey();
	return stream;
}

namespace std
{
	std::string to_string(Key const& k)
	{
		return std::to_string(k.getKey());
	}
}

int main()
{
	auto seed = std::chrono::system_clock::now().time_since_epoch().count();
	std::mt19937 generator((unsigned short)seed);

	size_t size;
	do
	{
		std::cout << "Enter size:";
		std::cin >> size;
		if (size > 0)
		{
			BinarySearchTree<Key, unsigned short> tree;
			while (tree.size() < size)
			{
				unsigned short n = generator();

				Key key(n);

				tree.insert(key, n);

			}
			if (tree.size() <= 100)
				std::cout << tree;

			Key::resetCounter();
			unsigned short i;
			for (i = 0; i < 10; ++i)
			{
				unsigned short n;
				unsigned short* ble;
				do {
					n = generator();
					Key key(n);
					ble = tree.find(Key(key));
				} while (ble == nullptr);


				Key::resetCounter();
				Key key(n);
				Benchmark<std::chrono::nanoseconds> b(true);

				unsigned short foundValue = *tree.find(Key(key));
				std::cout << foundValue;
				std::cout << "Cmp count: " << Key::getCmpCount() << "\n";

			};

		}
	} while (size > 0);
	return 0;
}
