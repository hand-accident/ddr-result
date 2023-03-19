<script>
    import BadgeOutline from "../cell/BadgeOutline.svelte";
    import CardActionsEnd from "../cell/CardActionsEnd.svelte";
    import CardBase100Snap from "../cell/CardBase100Snap.svelte";
    import CardBody from "../cell/CardBody.svelte";
    import CardTitle from "../cell/CardTitle.svelte";
    import Rows from "../cell/Rows.svelte";
    import Text3xl from "../cell/Text3xl.svelte";
    import TextXl from "../cell/TextXl.svelte";
    import TextXs from "../cell/TextXs.svelte";
    import Truncate from "../cell/Truncate.svelte";
    import DifficultyBadge from "../group/DifficultyBadge.svelte";

    export let name, kind;
</script>

<CardBase100Snap class="">
    <CardTitle class="l0">
        <Rows class="l1">
            <Truncate class="">{name}</Truncate>
            <DifficultyBadge {kind} class="" />
        </Rows>
    </CardTitle>
    <CardBody class="l2">
        <Text3xl class="l3">
            <slot name="score" />
        </Text3xl>
        <TextXl class="l4">
            <slot name="bpmMain" />
        </TextXl>
        <TextXs class="l5">
            <slot name="bpmSub" />
        </TextXs>
        <CardActionsEnd class="l6">
            <BadgeOutline class="">
                <slot name="clearDate" />
            </BadgeOutline>
            <BadgeOutline class="">
                <slot name="availability" />
            </BadgeOutline>
        </CardActionsEnd>
    </CardBody>
</CardBase100Snap>

<style lang="postcss" module>
    .l0 {
        @apply m-4;
    }
    .l1 {
        @apply w-full justify-between;
    }
    .l2 {
        @apply py-0 gap-y-0;
    }
    .l3 {
        @apply mt-2 mb-1 flex-grow;
    }
    .l4 {
        @apply flex-grow;
    }
    .l5 {
        @apply mb-2 flex-grow;
    }
    .l6 {
        @apply mb-2;
    }
</style>
