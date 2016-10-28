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
  uint[] public publicKey;


  // Contract constructor
  function Ballot(
    string ballotTitle,
    string ballotDescription,
    string ballotCandidates,
    address[] eligableVoters,
    uint ballotDuration,
    uint[] ballotPublicKey
  ) {

    // Set the internal variables
    title = ballotTitle;
    description = ballotDescription;
    voters = eligableVoters;
    deadline = now + ballotDuration;
    publicKey = ballotPublicKey;

    // Deserialise the candidates string
    deserialiseCandidates(ballotCandidates);
  }

  // TODO Get the public key of the ballot
  function getPublicKey() returns (uint[] publicKey) {

  }

  // TODO Vote in the ballot
  function vote(uint[] votes) returns (bool success) {

  }

  // TODO Get the result of the ballot
  function result() returns (int[] votes) {

  }

  // TODO Deserialise a candidates string into the internal array
  function deserialiseCandidates(string candidatesString) {

  }
}
