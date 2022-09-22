//Moralissss
const serverUrl = "https://imxtw7bo0qqy.usemoralis.com:2053/server";
const appId = "F91xFTIo5SvKAEQoDK1eU682BdtLaf5AK4Qf1Xhw";
console.log(Moralis);
Moralis.start({ serverUrl, appId });

async function login() {
  let user = Moralis.User.current();
  const chainId = await Moralis.chainId;
  console.log(chainId);
  console.log(user);
  if (!user) {
    user = await Moralis.authenticate({
      provider: "walletconnect",
      chainId: chainId,
      signingMessage: "Login to initialize Vicky",
    })
      .then(async function (user) {
        console.log("logged in user: " + user.get("ethAddress"));
        const options = {
          chain: "mumbai",
          address: user.get("ethAddress"),
          token_address: "0x3cE643dc61bb40bB0557316539f4A93016051b81",
        };
        const polygonNFTs = await Moralis.Web3API.account.getNFTs(options);
        ConnectDialogVisibility(false);
        console.log(polygonNFTs);
        let hasLicense = false;
        let myApps = [];
        polygonNFTs.result.forEach((element) => {
          let metadata = JSON.parse(element.metadata);
          if (
            metadata.name === "Vicky Stocks" ||
            metadata.name === "Vicky-weather" ||
            metadata.name === "Vicky Jokes" ||
            metadata.name === "vicky recipes"
          ) {
            myApps.push(metadata.name);
            hasLicense = true;
          }
        });
        eel.setApps(myApps);
        if (!hasLicense) {
          NoLicenseDialogVisibility(true);
        }
      })
      .catch(function (error) {
        console.log(error);
        ConnectDialogVisibility(true);
      });
  } else {
    document.getElementById("connect-wallet-dialog").style.display = "none";
  }
}

async function logout() {
  await Moralis.User.logOut();
  console.log("logged out");
}

function ConnectDialogVisibility(isOpen) {
  if (isOpen === true) {
    document.getElementById("connect-wallet-dialog").style.display = "flex";
  } else {
    document.getElementById("connect-wallet-dialog").style.display = "none";
  }
}

function NoLicenseDialogVisibility(isOpen) {
  if (isOpen === true) {
    document.getElementById("no-license-dialog").style.display = "flex";
  } else {
    document.getElementById("no-license-dialog").style.display = "none";
  }
}

function PurchaseDialogVisibility(isOpen) {
  if (isOpen === true) {
    document.getElementById("pricing").style.display = "flex";
  } else {
    document.getElementById("pricing").style.display = "none";
  }
}

function UploadDialogVisibility(isOpen) {
  if (isOpen === true) {
    document.getElementById("upload-dialog").style.display = "flex";
  } else {
    document.getElementById("upload-dialog").style.display = "none";
  }
}

async function buy(app) {
  alert("Buying");
  //project id: "115481951119335216980278182891761464945475745406529462616472332953425351720030"
  const address = Moralis.User.current().get("ethAddress");
  const ABI = [
    {
      inputs: [{ internalType: "address", name: "_registry", type: "address" }],
      stateMutability: "nonpayable",
      type: "constructor",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: true,
          internalType: "address",
          name: "account",
          type: "address",
        },
        {
          indexed: true,
          internalType: "address",
          name: "operator",
          type: "address",
        },
        {
          indexed: false,
          internalType: "bool",
          name: "approved",
          type: "bool",
        },
      ],
      name: "ApprovalForAll",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: false,
          internalType: "uint256",
          name: "_projectID",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_token",
          type: "address",
        },
        {
          indexed: false,
          internalType: "uint256",
          name: "_balance",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_recipient",
          type: "address",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_sender",
          type: "address",
        },
      ],
      name: "BalanceWithdrawn",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: false,
          internalType: "uint256",
          name: "_projectID",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "uint256",
          name: "_limit",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_sender",
          type: "address",
        },
      ],
      name: "LimitChanged",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: false,
          internalType: "uint256",
          name: "_projectID",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_token",
          type: "address",
        },
        {
          indexed: false,
          internalType: "uint256",
          name: "_price",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_sender",
          type: "address",
        },
      ],
      name: "PriceChanged",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: false,
          internalType: "uint256",
          name: "_projectID",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_token",
          type: "address",
        },
        {
          indexed: false,
          internalType: "uint256",
          name: "_price",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_recipient",
          type: "address",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_sender",
          type: "address",
        },
      ],
      name: "ProductPurchased",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: false,
          internalType: "uint256",
          name: "_projectID",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_recipient",
          type: "address",
        },
        {
          indexed: false,
          internalType: "uint256",
          name: "_amount",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "address",
          name: "_sender",
          type: "address",
        },
      ],
      name: "RoyaltyChanged",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: true,
          internalType: "address",
          name: "operator",
          type: "address",
        },
        {
          indexed: true,
          internalType: "address",
          name: "from",
          type: "address",
        },
        {
          indexed: true,
          internalType: "address",
          name: "to",
          type: "address",
        },
        {
          indexed: false,
          internalType: "uint256[]",
          name: "ids",
          type: "uint256[]",
        },
        {
          indexed: false,
          internalType: "uint256[]",
          name: "values",
          type: "uint256[]",
        },
      ],
      name: "TransferBatch",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: true,
          internalType: "address",
          name: "operator",
          type: "address",
        },
        {
          indexed: true,
          internalType: "address",
          name: "from",
          type: "address",
        },
        {
          indexed: true,
          internalType: "address",
          name: "to",
          type: "address",
        },
        {
          indexed: false,
          internalType: "uint256",
          name: "id",
          type: "uint256",
        },
        {
          indexed: false,
          internalType: "uint256",
          name: "value",
          type: "uint256",
        },
      ],
      name: "TransferSingle",
      type: "event",
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: false,
          internalType: "string",
          name: "value",
          type: "string",
        },
        {
          indexed: true,
          internalType: "uint256",
          name: "id",
          type: "uint256",
        },
      ],
      name: "URI",
      type: "event",
    },
    {
      inputs: [
        { internalType: "address", name: "account", type: "address" },
        { internalType: "uint256", name: "id", type: "uint256" },
      ],
      name: "balanceOf",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "address[]",
          name: "accounts",
          type: "address[]",
        },
        { internalType: "uint256[]", name: "ids", type: "uint256[]" },
      ],
      name: "balanceOfBatch",
      outputs: [{ internalType: "uint256[]", name: "", type: "uint256[]" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
      ],
      name: "getBalance",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "contract IERC20",
          name: "_token",
          type: "address",
        },
        { internalType: "uint256", name: "_projectID", type: "uint256" },
      ],
      name: "getBalance",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
      ],
      name: "getLimit",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "contract IERC20",
          name: "_token",
          type: "address",
        },
        { internalType: "uint256", name: "_projectID", type: "uint256" },
      ],
      name: "getPrice",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
      ],
      name: "getPrice",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
      ],
      name: "getSupply",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "address", name: "account", type: "address" },
        { internalType: "address", name: "operator", type: "address" },
      ],
      name: "isApprovedForAll",
      outputs: [{ internalType: "bool", name: "", type: "bool" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [],
      name: "name",
      outputs: [{ internalType: "string", name: "", type: "string" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [],
      name: "owner",
      outputs: [{ internalType: "address payable", name: "", type: "address" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [],
      name: "protocolFee",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        { internalType: "address", name: "_recipient", type: "address" },
      ],
      name: "purchase",
      outputs: [],
      stateMutability: "payable",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "contract IERC20",
          name: "_token",
          type: "address",
        },
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        { internalType: "address", name: "_recipient", type: "address" },
      ],
      name: "purchase",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [],
      name: "registry",
      outputs: [
        { internalType: "contract Registry", name: "", type: "address" },
      ],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        { internalType: "uint256", name: "_price", type: "uint256" },
      ],
      name: "royaltyInfo",
      outputs: [
        { internalType: "address", name: "", type: "address" },
        { internalType: "uint256", name: "", type: "uint256" },
      ],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "address", name: "from", type: "address" },
        { internalType: "address", name: "to", type: "address" },
        { internalType: "uint256[]", name: "ids", type: "uint256[]" },
        { internalType: "uint256[]", name: "amounts", type: "uint256[]" },
        { internalType: "bytes", name: "data", type: "bytes" },
      ],
      name: "safeBatchTransferFrom",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        { internalType: "address", name: "from", type: "address" },
        { internalType: "address", name: "to", type: "address" },
        { internalType: "uint256", name: "id", type: "uint256" },
        { internalType: "uint256", name: "amount", type: "uint256" },
        { internalType: "bytes", name: "data", type: "bytes" },
      ],
      name: "safeTransferFrom",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        { internalType: "address", name: "operator", type: "address" },
        { internalType: "bool", name: "approved", type: "bool" },
      ],
      name: "setApprovalForAll",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        { internalType: "uint256", name: "_limit", type: "uint256" },
      ],
      name: "setLimit",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "address payable",
          name: "_owner",
          type: "address",
        },
      ],
      name: "setOwner",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "contract IERC20",
          name: "_token",
          type: "address",
        },
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        { internalType: "uint256", name: "_price", type: "uint256" },
      ],
      name: "setPrice",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        { internalType: "uint256", name: "_price", type: "uint256" },
      ],
      name: "setPrice",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "uint256",
          name: "_protocolFee",
          type: "uint256",
        },
      ],
      name: "setProtocolFee",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [{ internalType: "address", name: "_registry", type: "address" }],
      name: "setRegistry",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        { internalType: "address", name: "_recipient", type: "address" },
        { internalType: "uint256", name: "_amount", type: "uint256" },
      ],
      name: "setRoyalty",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [{ internalType: "bytes4", name: "interfaceId", type: "bytes4" }],
      name: "supportsInterface",
      outputs: [{ internalType: "bool", name: "", type: "bool" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [],
      name: "symbol",
      outputs: [{ internalType: "string", name: "", type: "string" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
      ],
      name: "uri",
      outputs: [{ internalType: "string", name: "", type: "string" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        {
          internalType: "address payable",
          name: "_recipient",
          type: "address",
        },
      ],
      name: "withdraw",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      inputs: [
        {
          internalType: "contract IERC20",
          name: "_token",
          type: "address",
        },
        { internalType: "uint256", name: "_projectID", type: "uint256" },
        {
          internalType: "address payable",
          name: "_recipient",
          type: "address",
        },
      ],
      name: "withdraw",
      outputs: [],
      stateMutability: "nonpayable",
      type: "function",
    },
  ];
  let projectID = null;
  let _msgValue = (0 * 1000000000000000000).toString();
  switch (app) {
    case "recipes":
      projectID =
        "43931014182185514038404861646576613527570967730078004044376888033594158509601";
      _msgValue = (0.1 * 1000000000000000000).toString();
      break;
    case "weather":
      projectID =
        "81994587989992619171820055711032055418059131404544288173916442902830447958124";
      break;
    case "jokes":
      projectID =
        "66956813426678163643190640437541922871317051322956188906411966005028597439015";
      break;
    case "stocks":
      projectID =
        "7678235331578057208434875357077070104058881615202953206983147281935578660662";
      _msgValue = (0.001 * 1000000000000000000).toString();
      break;
    default:
      break;
  }
  const sendOptions = {
    contractAddress: "0x3cE643dc61bb40bB0557316539f4A93016051b81",
    functionName: "purchase(uint256,address)",
    abi: ABI,
    params: {
      _projectID: projectID,
      _recipient: address,
    },
    msgValue: Moralis.Units.ETH(_msgValue),
  };

  const transaction = await Moralis.executeFunction(sendOptions);
  console.log(transaction.hash);
  // --> "0x39af55979f5b690fdce14eb23f91dfb0357cb1a27f387656e197636e597b5b7c"

  // Wait until the transaction is confirmed
  await transaction.wait();
  console.log("Txn completed");
}

/**                SAVING                                        */
let app = {};
function handleSignUpInput() {
  app.appName = document.getElementById("app-name-input").value;
  app.appFile = document.getElementById("app-file-input").files[0];

  console.log(app);
}

function handleFormSubmit() {
  console.log(JSON.stringify(app));
  saveIPFS(app.appName, app);
}

async function saveIPFS(name, item) {
  //upload File
  let file = new Moralis.File(name, item.appFile);
  await file.saveIPFS();
  console.log(file.ipfs(), file.hash());

  let appRef = {
    appName: item.appName,
    appFileHash: file.hash(),
    appFileUrl: file.ipfs(),
  };
  let file2 = new Moralis.File(name, { base64: btoa(JSON.stringify(appRef)) });
  await file2.saveIPFS();
  console.log(file2.ipfs(), file2.hash());
  return file2.ipfs();
}
