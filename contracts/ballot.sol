pragma solidity ^0.4.2;

// Blockchain Ballot Contract
// Test data: "title", "desc", "candidate1,candidate2,candidate3", 3, ["0x25772ddc83fbb9fb5b6efc80126c41c111691804", "0x8129210630afa5501955dbf47ae7cf84139d065e", "0xca2b2e8df476a129417d38ab4172c62079d1bd28", "0xca35b7d915458ef540ade6068dfe2f44e8fa733c"], ["5064e7d2d7d6b7f93a2dd3914d6ea98433a18e02806f009f7a62fd3f5a7847b7", "a0bec32fb941be60dbe9a45a522cc487200ff0b0e47e17e0727d2891cbe43092", "00ad06460848c2cc1afdd5d14cc6c74d9bc2e6bee6e17f0bf5fb68c78cd7fb6d", "449f4ebf2e2b1a3eb1e8b4e2cec01c1fbc284d19d57d1285e8600f2af4dc4d75"], ["6c5e0797c3468ba13b807ca23b8aa0886f83a76d348f9f54cde78977cfb79a81", "29815ef1059b88f8a94e088ca1732a5292884024855d7a7ef6d9667352f36ee6", "2d7bf8c3979c543ac9cd23edd27657fe92832f79a028a7e9cd9a3670a3a9f71a", "4e533a5f80465284476c5024599115f46fe823f4f4f2d6cabbb8f82cdf60f850"]
// title = 'title'; description = 'description'; candidates = 'Donald J Trump,Hilary Clinton,Gary Johnson'; voters = "25772ddc83fbb9fb5b6efc80126c41c111691804,8129210630afa5501955dbf47ae7cf84139d065e,ca2b2e8df476a129417d38ab4172c62079d1bd28" ["0x25772ddc83fbb9fb5b6efc80126c41c111691804", "0x8129210630afa5501955dbf47ae7cf84139d065e", "0xca2b2e8df476a129417d38ab4172c62079d1bd28"]; publicKeyN = [36363312580864531061336973206242688290453132382537635816604564722874205095863, 72707103842795452012333280058084468430497690680563862448909977989266901577874, 305707840753438375496830897586809708835872169162463123246986456395444386669, 31038745877388837372214016003236662609189093538267774859806823607192226909557]; publicKeyG = [36363312580864531061336973206242688290453132382537635816604564722874205095863, 72707103842795452012333280058084468430497690680563862448909977989266901577874, 305707840753438375496830897586809708835872169162463123246986456395444386669, 31038745877388837372214016003236662609189093538267774859806823607192226909558];
contract Ballot {

  // Public variables of the ballot
  string public title;
  string public description;
  string public candidates;
  uint public candidatesCount;
  address[] public voters;
  mapping (address => bool) public hasVoted;
  uint[] public publicKeyN;
  uint[] public publicKeyG;
  uint[] public votes;

  // Contract constructor
  function Ballot(string _title, string _description, string _candidates, uint _candidatesCount, address[] _voters, uint[] _publicKeyN, uint[] _publicKeyG) {

    // Set the basic variables
    title = _title;
    description = _description;
    candidates = _candidates;
    candidatesCount = _candidatesCount;

    // Loop through each voter address
    uint index = 0;
    for (index = 0; index < _voters.length; index++) {

      // Add the address to the voters array
      voters.push(_voters[index]);

      // Initalise the voter has voted flag
      hasVoted[_voters[index]] = false;
    }

    // Loop through each chunk of the public key 'n'
    for (index = 0; index < _publicKeyN.length; index++) {

      // Add the chunk to the complete array
      publicKeyN.push(_publicKeyN[index]);
    }

    // Loop through each chunk of the public key 'g'
    for (index = 0; index < _publicKeyG.length; index++) {

      // Add the chunk to the complete array
      publicKeyG.push(_publicKeyG[index]);
    }
  }

  // Get the voters of the ballot
  function getVoters() constant returns (address[]) { return voters; }

  // Get the public key 'n' of the ballot
  function getPublicKeyN() constant returns (uint[]) { return publicKeyN; }

  // Get the public key 'g' of the ballot
  function getPublicKeyG() constant returns (uint[]) { return publicKeyG; }

  // Get the votes in the ballot
  function getVotes() constant returns (uint[]) { return votes; }

  // Vote in the ballot
  function executeVote(uint[] vote) returns (bool sucess) {

    // Get the address attempting to voters
    address sender = msg.sender;

    // Loop through each voter
    for (uint index = 0; index < voters.length; index++) {

      // Check if this voter is the sender
      if (sender == voters[index]) {

        // Check if this voter has already voted
        if(!hasVoted[sender]) {

          // Check the vote is of the correct length
          // Each vote is 2056 bits long represented in 8 256 bit integers
          if(vote.length == candidatesCount * 8) {

              // Loop through the votes
              for (index = 0; index < vote.length; index++) {

                // Add this vote
                votes.push(vote[index]);

                // Mark this voter as having now voted
                hasVoted[sender] = true;
              }

              // The vote action was successful
              return true;
          }
        }
      }
    }

    // Sender is not a valid voter
    return false;
  }
}
