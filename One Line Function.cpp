// This's a way to create a single line function in C++
const auto FUNC_NAME = [] (const auto &PARM_NAME) { /* CODE_OF_BLOCK */};
//Example
const auto isPositive = [] (const auto &val) { return val > 0 ? "Positive" : "Negative"};
