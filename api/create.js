export default async function handler(req, res) {
    const { user } = req.query;

    // Replace with your Discord Webhook URL
    const webhook = "https://discord.com/api/webhooks/1494254904116645928/txJ-OkbAKhlOjvgfcbqMnkfPhaSmuu1P4HET_Rj04-wfMNbGBYhTrhwCvfcxhhDCyzCG";

    await fetch(webhook, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            content: `!trigger_ai ${user}`
        })
    });

    // A clean "Success" page for your laptop browser
    res.setHeader('Content-Type', 'text/html');
    res.send('<h1>📡 Syncing with UAE Node... Check DMs</h1><script>setTimeout(()=>window.close(), 1500)</script>');
}
