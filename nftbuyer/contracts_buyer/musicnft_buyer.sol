pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract BeatBlocks1 is ERC721Full {
    using SafeMath for uint;

    address payable owner = msg.sender;
    string public symbol = "BTBS1";
    uint public exchange_rate = 100;
    uint public backstage_pass = 50;
    
    mapping(address => uint) balances;
    
    constructor() public ERC721Full("BeatBlocks1", "BTBS1") {}

    function registerAudio(address owner, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        return tokenId;
    }
    
    
// #transferFrom
// #balanceOf
// #totalSupply
// #successful statement

    funciton get_type()
    
    function get_perks()
    
    
    function balanceOf() public view returns(uint) {
        return balances[msg.sender];
    }

    function transferFrom(address recipient, uint value) public {
        balances[msg.sender] = balances[msg.sender].sub(value);
        balances[recipient] = balances[recipient].add(value);
    }
    
    function purchase() public payable {
        uint amount = msg.value * exchange_rate;
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }
    
     function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        balances[recipient] += value;
    }
}