pragma solidity ^0.4.2;

// Blockchain Ballot Contract
contract Ballot {

  // Public variables of the ballot
  string public version = 'Blockchain Ballot | Version 0.1';
  string public title;
  string public description;
  string[] public candidates;
  address[] public voters;
  uint public duration;
  uint public deadline;
  mapping (address => bool) public hasVoted;


  // Contract constructor
  function Ballot(
    string title,
    string description,
    string candidates,
    address[] voters,
    uint duration
  ) {
    title = title;
    description = description;
    // TODO Deserialise candidates string to array
    // candidates = candidates;
    voters = voters;
    deadline = now + duration;
  }

  // TODO Vote in the ballot
  function vote(uint[] votes) returns (bool success){

  }

  // TODO Get the result of the ballot
  function result() returns (int[] votes){

  }
}
