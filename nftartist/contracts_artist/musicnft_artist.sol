pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract BeatBlocks is ERC721Full {
    using SafeMath for uint;

    address payable owner = msg.sender;
    string public symbol = "BTBS";
    uint public exchange_rate = 100;
    
    mapping(address => uint) balances;
    
    constructor() public ERC721Full("BeatBlocks", "BTBS") {}

    function registerAudio(address owner, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        return tokenId;
    }
    
    function contractURI() public view returns (string memory) {
        return "https://gateway.pinata.cloud/ipfs/QmRYV8ZYoS2bJun1WULynfgkLxkmZSgqUPEs13eRWDPoFq";
    }

}