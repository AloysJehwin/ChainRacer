// app.js

// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
}

document.getElementById('connectWallet').addEventListener('click', async () => {
    // Request account access from MetaMask
    try {
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        const account = accounts[0];
        console.log('Connected account:', account);
        alert(`Connected to account: ${account}`);
    } catch (error) {
        console.error('Error connecting to MetaMask', error);
    }
});
