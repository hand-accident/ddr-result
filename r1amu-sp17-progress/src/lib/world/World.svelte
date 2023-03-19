<script>
    import Header from "./Header.svelte";
    import Footer from "./Footer.svelte";
    import ChartCards from "./ChartCards.svelte";
    import ConfigMenu from "./ConfigMenu.svelte";
    import { Config } from "../arith/Classes.svelte";
    import { updateDate } from "../../updateDate.json";

    let config = new Config({ cleared: true, playable: true });
</script>

<ConfigMenu bind:config>
    <Header date={updateDate} />
    <ChartCards {config} />
    <Footer />
</ConfigMenu>
